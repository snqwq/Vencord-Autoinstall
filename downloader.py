import requests
import hashlib
import pathlib

def download_and_verify(install_path: pathlib.Path) -> tuple[bool, pathlib.Path | None]:
    exe_path = install_path / "VencordInstallerCli.exe"

    # Get the latest release data from the GitHub API
    response = requests.get(
        "https://api.github.com/repos/Vencord/Installer/releases/latest"
    )
    data = response.json()

    # Extract the download URLs
    assets = data["assets"]
    download_url = None
    checksums_url = None
    for asset in assets:
        if asset["name"] == "VencordInstallerCli.exe":
            download_url = asset["browser_download_url"]
        elif asset["name"] == "checksums.sha256":
            checksums_url = asset["browser_download_url"]

    if not download_url or not checksums_url:
        print("Could not find required assets in release")
        return False, None

    # Get expected hash
    checksums_response = requests.get(checksums_url)
    expected_hash = None
    for line in checksums_response.text.splitlines():
        if "VencordInstallerCli.exe" in line:
            expected_hash = line.split()[0]
            break

    if not expected_hash:
        print("Could not find checksum for VencordInstallerCli.exe")
        return False, None

    # If already exists, check it against the remote checksum first
    if exe_path.exists():
        actual_hash = hashlib.sha256(exe_path.read_bytes()).hexdigest()
        if actual_hash == expected_hash:
            print("Installer already present and verified.")
            return True, exe_path
        else:
            print("Installer checksum mismatch, redownloading...")

    # Download and verify
    installer_response = requests.get(download_url)
    actual_hash = hashlib.sha256(installer_response.content).hexdigest()
    if actual_hash == expected_hash:
        print("Installer verified successfully.")
        with open(exe_path, "wb") as f:
            f.write(installer_response.content)
        return True, exe_path
    else:
        print("Installer verification failed after download.")
        return False, None