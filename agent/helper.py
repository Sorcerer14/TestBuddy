import platform
import getpass
import socket

def get_system_details() -> dict:
    """
    Returns basic system details useful for tech support.
    """
    try:
        details = {
            "os": platform.system(),
            "os_version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "hostname": socket.gethostname(),
            "ip_address": socket.gethostbyname(socket.gethostname()),
            "username": getpass.getuser(),
            "python_version": platform.python_version(),
        }
        return {"status": "success", "system_info": details}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
    

def save_json_file():
    # Aditya try writing some code here to save the gemini response to a json file and save it in the current folder, better create a new folder named "data" and save it there.
    pass
    

