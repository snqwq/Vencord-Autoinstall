import subprocess
import pathlib
import platform

if platform.system() != "Windows":
    print("sorry this only works on windows rn")
    exit(1)


installer_path = "VencordInstallerCli.exe"

result = subprocess.run(
    [installer_path, "-repair", "-branch", "auto"]
)