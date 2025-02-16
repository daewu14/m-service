import argparse
from cmd import http, migrations, db_check


class _m_parser:
    name: str


def run():
    cmd_action = [
        http.HttpCommand,
        db_check.DBCheck,
        migrations.MigrationsCommand,
    ]

    parser = argparse.ArgumentParser(description="M-Service CLI tools")

    # Add subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", required=False, help="Available subcommands")
    for action in cmd_action:
        action = action()
        subparser = subparsers.add_parser(action.name, help=action.help, description=action.description)
        action.sub(subparser)

    args = parser.parse_args()
    for action in cmd_action:
        action = action()
        if action.name == args.command:
            action.run(parser=parser)
