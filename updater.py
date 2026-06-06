import subprocess
import pathlib
import platform
import datetime
import sys

# platform check until linux support
if platform.system() != "Windows":
    print("sorry this only works on windows rn")
    exit(1)

if getattr(sys, "frozen", False):

    base_dir = pathlib.Path(sys.executable).parent
else:

    base_dir = pathlib.Path(__file__).parent


installer_path = base_dir / "VencordInstallerCli.exe"

result = subprocess.run(
    [installer_path, "-repair", "-branch", "auto"],
    capture_output=True,
    text=True
)


with open("output.log", "a") as f:
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(t + "\n")
    f.write(result.stdout)
    f.write(result.stderr)