import subprocess
import platform

def check_task_exists(task_name):
    if platform.system() != "Windows":
        print("sorry this only works on windows rn")
        return False

    command = f'schtasks /Query /TN "{task_name}"'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    return result.returncode == 0

def register_task(task_name, script_path):
    if platform.system() != "Windows":
        print("sorry this only works on windows rn")
        return False

    if check_task_exists(task_name):
        print(f"Task '{task_name}' already exists.")
        return True

    command = f'schtasks /Create /TN "{task_name}" /TR "{script_path}" /SC DAILY /ST 00:00'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    if result.returncode == 0:
        print(f"Task '{task_name}' registered successfully.")
        return True
    else:
        print(f"Failed to register task '{task_name}'. Error: {result.stderr}")
        return False

def unregister_task(task_name):
    if platform.system() != "Windows":
        print("sorry this only works on windows rn")
        return False

    command = f'schtasks /Delete /TN "{task_name}" /F'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    if result.returncode == 0:
        print(f"Task '{task_name}' unregistered successfully.")
        return True
    else:
        print(f"Failed to unregister task '{task_name}'. Error: {result.stderr}")
        return False