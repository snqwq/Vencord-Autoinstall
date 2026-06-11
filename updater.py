import subprocess
import pathlib
import platform
import datetime
import sys

import downloader
import scheduler

logger = []

# platform check until linux support
if platform.system() != "Windows":
    print("sorry this only works on windows rn")
    logger.append("unsupported platform")
    exit(1)


# check if executable is packaged
if getattr(sys, "frozen", False):

    self_path = pathlib.Path(sys.executable)
    base_dir = pathlib.Path(sys.executable).parent
else:
    self_path = pathlib.Path(__file__)
    base_dir = pathlib.Path(__file__).parent


installer_downloaded, installer_path = downloader.download_and_verify(base_dir)
if not installer_downloaded:
    exit(1)

if scheduler.check_task_exists("VencordAutoUpdate"):
    print("Task already exists, skipping registration.")
    logger.append("Task already exists")
else:
    scheduler.register_task("VencordAutoUpdate", str(self_path))

result = subprocess.run(
    [str(installer_path), "-repair", "-branch", "auto"], capture_output=True, text=True
)


with open("output.log", "a") as f:
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(
        t
        + "\n begin vencord cli output\n"
        + result.stdout
        + "\n"
        + result.stderr
        + "\n end vencord cli output\n\n"
    )
    f.write("log:\n")
    for entry in logger:
        f.write(f" - {entry}\n")
