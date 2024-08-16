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
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
Do you have RDP or VDI access, but no copy/paste, no outbound network, and need to exfiltrate some sensitive data? 
This tool provides a method to reliably move files from restricted environments such as these to your own machine.
It's web-based, circumventing client-side security controls such as AV/EDR or application control, and usually performant enough to transfer moderately large files (50MB) in a reasonable amount of time (a few hours).

### Installation
What you need:
 - Some kind of desktop session on a remote machine

If you need to transfer files from a restricted physical machine as well:
 - A laptop to receive
 - USB video capture card
 - HDMI cable

```bash
git clone https://github.com/hack3n/qr-exfil
```

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact

Project Link: [https://github.com/hack3n/qr-exfil](https://github.com/hack3n/qr-exfil)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/hack3n/qr-exfil.svg?style=for-the-badge
[issues-url]: https://github.com/hack3n/qr-exfil/issues
[license-shield]: https://img.shields.io/github/license/hack3n/qr-exfil.svg?style=for-the-badge
[license-url]: https://github.com/hack3n/qr-exfil/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/liam-o-brien-017aa6178/
