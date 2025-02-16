import glob
import os


# Function to execute Python files and extract their variables
def read_get_variables(folder_path):
    # Create a dictionary to store variables and values
    variables = {}

    # Get all Python files in the folder
    py_files = glob.glob(os.path.join(folder_path, '*.py'))

    for py_file in py_files:
        # Prepare a dictionary to store variables from this specific file
        file_variables = {}

        # Open and execute the file in the current context
        with open(py_file, 'r') as file:
            code = file.read()
            # Use exec() to execute the Python file's code in the file_variables context
            exec(code, {}, file_variables)

        # Add the extracted variables to the main variables dictionary
        variables[py_file] = file_variables

    return variables
