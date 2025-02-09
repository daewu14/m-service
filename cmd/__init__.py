import argparse
from cmd import http, migrations

def run():
    cmd_action = {
        'http': http.run,
        'migrations': migrations.run,
    }

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="list available command : "+", ".join(cmd_action.keys()))
    args = parser.parse_args()

    command = cmd_action.get(args.command, None)

    if command is None:
        print("Command not found, list available command :\n - "+"\n - ".join(cmd_action.keys()))
        exit(0)

    command()