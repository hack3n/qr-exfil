import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import base64
import urllib.request
import json
from PIL import ImageGrab

def capture_screen():
    screenshot = ImageGrab.grab()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    return frame

def detect_qr_codes(frame):
    decoded_objects = pyzbar.decode(frame, symbols=[pyzbar.ZBarSymbol.QRCODE])
    return decoded_objects


def main():
    chunk_data = []
    previous_identifier = -1

    print("qr-exfil by hack3n")
    print("ctrl+c once all QR codes have been displayed and read")
    
    try:
        while True:
            frame = capture_screen()
            qr_codes = detect_qr_codes(frame)
            
            for qr_code in qr_codes:
                data = qr_code.data.decode("utf-8")
                
                if data not in chunk_data:
                    if data == "START":
                        print("[+] Starting read")
                        continue

                    identifier = int(data[:data.index("#")])
                    if previous_identifier + 1 != identifier:
                        print("[!] Chunk missed")
                        
                    print(f"[+] New data appended ({identifier})")
                    chunk_data.append(data)
                    previous_identifier = identifier

    except KeyboardInterrupt:                    
        with open("raw.json", "w") as f:
            f.write(json.dumps(chunk_data, indent=4))
        print("[+] Dumped raw reads")
        print("[+] Use util/dump-from-json.py to get the output file")

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
