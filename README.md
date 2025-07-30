<h1 align="center">MH-HP-Overlay-For-PSP-Emulator</h1>

<div align="center">

  [![StaticBadge](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
  [![App](https://img.shields.io/badge/App-1.0.0-green)](https://github.com/Alexander-Lancellott/MH-HP-Overlay-For-PSP-Emulator)

</div>

## Description

A simple open-source HP overlay that I've developed for MHF/2/U, MHP/2/G and MHP3/HD in Python. This project is a port of another one I previously created called [MH-HP-Overlay-For-3DS-Emulator](https://github.com/Alexander-Lancellott/MH-HP-Overlay-For-3DS-Emulator), but this time it's designed to work with PSP emulator, such as [PPSSPP](https://www.ppsspp.org/download/), on their PC (Windows) versions.

You can support me by donating! I’d really appreciate it. But either way, thank you for using this mod!

<a href='https://ko-fi.com/B0B115WKYH' target='_blank'>
  <img height='45' style='border:0px;height:45px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=6' border='0' alt='Buy Me a Coffee at ko-fi.com' />
</a>

## Building - (For Developers)

```
$ git clone
```

```
$ python -m venv .venv
$ .venv\Scripts\activate
$ pip install .
$ build
```
You will find the `build` in the `build/dist` folder

## Python modules used

- ahk[binary] - v1.8.0
- ahk-wmutil - v0.1.0
- colorama - v0.4.6
- PySide6 - v6.7.2
- Pymem - v1.13.1
- cx_Freeze - v8.0.0
- cursor - v1.3.5
- pywin32 - v306
- numpy - v2.2.4
- art - v6.2
- PyYAML - v6.0.2
- pcre2 - v0.5.2
