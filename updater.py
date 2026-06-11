import subprocess
import pathlib
import platform
import sys

import downloader
import scheduler
import logger

# check if executable is packaged
if getattr(sys, "frozen", False):

    self_path = pathlib.Path(sys.executable)
    base_dir = pathlib.Path(sys.executable).parent
else:
    self_path = pathlib.Path(__file__)
    base_dir = pathlib.Path(__file__).parent

log = logger.Logger(path=base_dir / "update.log")

# platform check until linux support
if platform.system() != "Windows":
    log.append("ERROR  unsupported platform")
    exit(1)

installer_downloaded, installer_path = downloader.download_and_verify(base_dir)
if not installer_downloaded:
    exit(1)

if scheduler.check_task_exists("VencordAutoUpdate"):
    log.append("INFO  Task already exists, skipping registration.")
else:
    scheduler.register_task("VencordAutoUpdate", str(self_path))


# run the installer with the -repair flag to update the existing installation
result = subprocess.run(
    [str(installer_path), "-repair", "-branch", "auto"], capture_output=True, text=True
)

log.append("vencord cli output:" + "\nstdout:\n" + result.stdout)
log.append("vencord cli error output:\n" + result.stderr)

log.save()
