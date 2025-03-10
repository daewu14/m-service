import glob
import os
import runpy

from pkg.logger.log import logger


# Function to execute Python files and extract their variables
def read_get_variables(folder_path):
    # Create a dictionary to store variables and values
    variables = {}

    # Get all Python files in the folder
    py_files = glob.glob(os.path.join(folder_path, '*.py'))

    for py_file in py_files:
        file_variables = {}
        result = runpy.run_path(py_file)
        # List all variables and their values in the result dictionary
        for var_name, var_value in result.items():
            file_variables[var_name] = var_value

        # Add the extracted variables to the main variables dictionary
        variables[py_file] = file_variables

    return variables


def check_folder_exists(folder_path):
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        return True
    else:
        return False


def create_folder(folder_path) -> [bool, str]:
    try:
        os.makedirs(folder_path, exist_ok=True)
        return [True, f"Folder '{folder_path}' created successfully"]
    except Exception as e:
        return [False, f"Error creating folder '{folder_path}': {str(e)}"]

def list_files_in_directory_without_extension(directory_path):
    try:
        # List all files in the specified directory
        files = os.listdir(directory_path)
        # Filter out directories, only keep files and remove their extensions
        file_names = [os.path.splitext(f)[0] for f in files if os.path.isfile(os.path.join(directory_path, f))]
        return file_names
    except Exception as e:
        logger.error(f"Error listing files", extra={
            "detail": str(e),
            "directory": directory_path
        })
        return []
