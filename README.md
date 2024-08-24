<a name="readme-top"></a>

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<h3>QR Exfil</h3>

<p>
  A web-based no-fix (?) tool to exfiltrate data from a restricted environment using QR codes.
  <br />
  <a href="#installation"><strong>Install »</strong></a>
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Do you have RDP or VDI access, but no copy/paste, no outbound network, and need to exfiltrate some sensitive data? 
This tool provides a method to reliably move files from restricted environments such as these to your own machine.
It's web-based, circumventing client-side security controls such as AV/EDR or application control, and usually performant enough to transfer moderately large files (50MB) in a reasonable amount of time (a few hours).

### Installation

Run the following:
```bash
git clone https://github.com/hack3n/qr-exfil
pip3 install pyzbar pillow pybase64 opencv-python
```

What you need:
 - Some kind of desktop session on a remote machine
 - A Flipper or a rubber ducky USB

If you need to transfer files from a restricted physical machine as well:
 - A laptop to receive
 - USB video capture card
 - HDMI cable

### Usage

Basic usage:
 - Prepare `qr-exfil.html` to display QR codes on your primary monitor, either within your remote session (RDP or VDI), or using a USB video capture card and displaying the camera on screen.
 - Run `reader.py` on your host.
 - Start the QR code output on the target.
 - Wait for it to complete, then exit with `CTRL + C`.
 - Use the `util\dump-from-json.py` script to get your output file on your host.

This repository includes a number of scripts and utilities that you may require:
 - `reader.py` - Reads your primary moniter for QR codes and dumps them to a `raw.json` file.
 - `qr-exfil.html` - The payload HTML that chunks and displays a local file in rotating QR codes.
 - `util\dump-from-json.py` - Reads the raw data from `raw.json` and outputs it to a file `output`.
 - `util\find-missing-ids.py` - Reads `raw.json` and checks that no chunks were missed by the reader.
 - `util\make-ducky.py` - Converts `qr-exfil.html` into a ruber ducky script payload to infil into your target environment.
 - `util\make-ducky-hex-string.py` - Sometimes VDI's can be sensitive with capital letters and special characters, so same as above, but as hex.
 - `util\decode-hex.html` - Intended to be manually typed out on the target environment to decode the hex inserted by the above script.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact

Project Link: [https://github.com/hack3n/qr-exfil](https://github.com/hack3n/qr-exfil)

## Acknowledgments

* [qrcodejs](https://github.com/davidshimjs/qrcodejs)


<!-- MARKDOWN LINKS & IMAGES -->
[issues-shield]: https://img.shields.io/github/issues/hack3n/qr-exfil.svg?style=for-the-badge
[issues-url]: https://github.com/hack3n/qr-exfil/issues
[license-shield]: https://img.shields.io/github/license/hack3n/qr-exfil.svg?style=for-the-badge
[license-url]: https://github.com/hack3n/qr-exfil/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/liam-o-brien-017aa6178/
