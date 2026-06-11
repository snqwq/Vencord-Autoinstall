# Vencord Autoinstall

an auto-running script to install and update vencord on startup.

[![asciicast](https://asciinema.org/a/c3jzNumOhhVveAe4.svg)](https://asciinema.org/a/c3jzNumOhhVveAe4)

![GitHub Release](https://img.shields.io/github/v/release/snqwq/Vencord-Autoinstall)
![GitHub repo size](https://img.shields.io/github/repo-size/snqwq/Vencord-Autoinstall)


[Download the latest release](https://github.com/snqwq/Vencord-Autoinstall/releases/latest)

> [!IMPORTANT]  
> This project is independently developed  in my free time. as with any third-party tool, use it at your own risk. this tool is persistent and will run on startup. security is not guaranteed, but I will do my best to ensure it is safe. the source code is available for review and contributions.

## Quick start

### Windows

just run the executable and it will set up everything for you.

### Linux

coming soon!

## Features

- auto install and update vencord on startup
- securely download and verify the installer
- minimal user interaction required (set it and forget it)

## How to build

```bash
pyinstaller --noconfirm --clean --name vencord_autoinstall --onedir updater.py
```

## How it works

excalidraw diagram here

## Credits

- [Vencord](https://vencord.dev/) ([github](https://github.com/Vencord))
- [Vencord Installer](https://github.com/Vencord/Installer)
