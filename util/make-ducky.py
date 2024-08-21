ducky_script = ""

with open("../qr-exfil.html", "r") as file:
    for line in file:
        if line.isspace(): continue
        ducky_script += f"STRING {line}"
        ducky_script += "ENTER\n"
        
with open("../qr-exfil-html.txt", "w") as file:
    file.write(ducky_script)