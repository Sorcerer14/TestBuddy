import platform
import getpass
import socket
import json
import os
import webbrowser
#from typing import Dict, Any, List

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
    


def save_json_file(json_data: str, filename: str = "test_cases.json") -> str:
    """
    Saves the provided JSON data (as a string) to a file within a 'data' subdirectory.

    Args:
        json_data: The JSON data, which will be passed by the model as a string.
        filename: The name of the file to save (default is 'test_cases.json').

    Returns:
        A string indicating the path where the file was saved.
    """
    # 1. Define the directory and file path
    output_dir = "data"
    output_path = os.path.join(output_dir, filename)

    # 2. Ensure the 'data' directory exists
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as e:
        return f"Error creating directory '{output_dir}': {e}"

    # 3. Handle data format: PARSE THE JSON STRING
    try:
        # The model provides a JSON string, so we must parse it here.
        data_to_save = json.loads(json_data)
    except json.JSONDecodeError:
        return "Error: Input data provided by the model is not valid JSON."

    # 4. Save the data to the JSON file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            # Use json.dump to write the Python object to the file
            json.dump(data_to_save, f, indent=4)
        return f"Successfully saved test cases to: {output_path}"
    except IOError as e:
        return f"Error writing file to '{output_path}': {e}"
    
    
def open_html_in_browser():
    """
    Opens the specified HTML file in the default web browser.

    Args:
        file_path: The path to the HTML file to open.
    """
    # Open the HTML file in the default web browser
    webbrowser.open_new_tab('http://127.0.0.1:5500/testBuddy.html')
    return "Opened testBuddy.html in the default web browser."
    

