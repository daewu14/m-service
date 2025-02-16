from datetime import datetime

from cmd import db_check
from cmd.abstract import AbstractCommand, argparse
from pkg.db.migration import initiate_migration
from pkg.logger.log import logger
from migrations import run


class MigrationsCommand(AbstractCommand):
    name = 'migration'
    description = 'Migrate all migrations'
    help = 'Migrate all migrations help'

    def sub(self, parser: argparse.ArgumentParser):
        parser.add_argument("--create", type=str, help="Create new migration")
        parser.add_argument("--migrate", help="Run migrations up/down")

    def run(self, parser: argparse.ArgumentParser):
        db_check.DBCheck().run(parser)
        args = parser.parse_args()

        # Register subcommands action
        self.create(args)
        self.migrate(args)

    def migrate(self, args):
        if args.migrate is None:
            return
        migrate = args.migrate
        logger.info("Running migration up")
        initiate_migration()

        if migrate in ("up", "down"):
            run(migrate)
        else:
            logger.error("Chose migrate option(up, down)")

    def create(self, args):
        if args.create is None:
            return
        input = args.create
        title = f"{input}".title()
        now = datetime.now()
        file_name = (f"{now.timestamp()}_{input}"
                     .lower()
                     .replace(" ", "_")
                     .replace(",", "")
                     .replace("*", "")
                     .replace(".", "_") + ".py")

        print(input)
        print(title)
        print(file_name)

        generate_python_file(f"migrations/{file_name}", template.format(
            filename=file_name,
            desc=title,
            date=now.strftime("%d.%m.%Y"),
            timestamp=now.timestamp()
        ))


# Template create migration
template = '''\
# {filename}
# Description: {desc}
# Generated by: dw_migrations
# Created on: {date}

# !!! Don't modify this variable !!!
timestamp = {timestamp}

# Migration up, modify here
sql_up = """

"""

# Migration down, modify here
sql_down = """

"""
'''

# Function to generate Python file from template
def generate_python_file(output_path, generated_code):
    # Write the generated code to the output file
    with open(output_path, 'w') as file:
        file.write(generated_code)

    print(f"Success generated python file at {output_path}")