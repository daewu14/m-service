import sys


def get_pyhton_usage() -> str:
    major_version = sys.version_info.major
    if major_version == 3:
        return "python3"
    else:
        return "python"