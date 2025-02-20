from cmd.abstract import AbstractCommand, argparse
from pkg.helper import py_version, py_execute


class UCase(AbstractCommand):
    name = 'ucase'
    description = 'Create new use case'
    help = f'{py_version.get_pyhton_usage()} run.py ucase -h'

    def sub(self, parser: argparse.ArgumentParser):
        parser.add_argument("new", type=str, help=f"{py_version.get_pyhton_usage()} run.py ucase new")

    def run(self, parser: argparse.ArgumentParser):
        args = parser.parse_args()

        registry_new = {
            'new': self.new_ucase,
            'update': self.add_update_ucase,
        }

        allowed_parse = registry_new.keys()
        if args.new not in allowed_parse:
            print(f"Un-support command {args.new}, please use : {', '.join(allowed_parse)}")
            return

        # execute command
        registry_new[args.new]()

    def fill_ucase(self, ucases=[], folder_name: str = ""):
        if len(ucases) > 0:
            ucase_name = input(f"New UCase name (fill empty & enter to execute) : ")
            ucase_exist = False
            for ucase in ucases:
                if ucase_name == ucase["name"]:
                    ucase_exist = True

            if ucase_exist:
                print(f"UCase name {ucase_name} already exists")
                return self.fill_ucase(ucases, folder_name)
            elif ucase_name == "":
                return ucases
            else:
                ucase_desc = input(f"Description for {ucase_name} : ")
                ucases.append({"name": ucase_name, "desc": ucase_desc})
                return self.fill_ucase(ucases, folder_name)
        else:
            ucase_name = input(f"New UCase name (on app/ucase/{folder_name}) : ")
            ucase_desc = input(f"Description for {ucase_name} : ")
            ucases.append({"name": ucase_name, "desc": ucase_desc})
            return self.fill_ucase(ucases, folder_name)
        pass

    def new_ucase(self):
        folder_name = input("Folder new ucase : ")
        if folder_name == "":
            print("Folder name is required")
            return
        print(f"Folder name : {folder_name}")

        folder_check = py_execute.check_folder_exists(f"app/ucase/{folder_name}")
        if folder_check:
            print(f"Folder already exists, please use another name")
            return

        [cf_ok, cf_message] = py_execute.create_folder(f"app/ucase/{folder_name}")
        if not cf_ok:
            print(cf_message)
            return

        # fill ucase process
        ucases = self.fill_ucase([], folder_name)

        ucases.append({"name": "__init__", "desc": "Init file"})

        for ucase in ucases:
            # Create and open the file in write mode
            with open(f"app/ucase/{folder_name}/{ucase['name']}.py", 'w') as file:
                # Write blank line
                if ucase['name'] == "__init__":
                    continue

                with open("cmd/ucase.template", "r") as read_file:
                    template = read_file.read()
                    rendered = template.replace("${ucase_folder}", folder_name).replace("${ucase_name}",
                                                                                        ucase["name"]).replace(
                        "${description}", ucase["desc"])
                    file.write(rendered)

        print(f"Success create new ucase {folder_name} with {len(ucases) - 1} ucase")
        pass

    def add_update_ucase(self):
        folder_name = input("Folder existing ucase : ")
        if folder_name == "":
            print("Folder name is required")
            return

        folder_check = py_execute.check_folder_exists(f"app/ucase/{folder_name}")
        if not folder_check:
            print(f"Folder doesn't exists, please use another name")
            return
        ucases = []
        # get existing ucase
        str_files = py_execute.list_files_in_directory_without_extension(f"app/ucase/{folder_name}")
        for i, file in enumerate(str_files):
            ucases.append({"name": file, "desc": None})

        # fill ucase process
        ucases = self.fill_ucase(ucases, folder_name)

        ucases_created = 0
        for ucase in ucases:
            # Write blank line
            if ucase['name'] in str_files:
                continue

            # Create and open the file in write mode
            with open(f"app/ucase/{folder_name}/{ucase['name']}.py", 'w') as file:

                with open("cmd/ucase.template", "r") as read_file:
                    template = read_file.read()
                    rendered = template.replace("${ucase_folder}", folder_name).replace("${ucase_name}",
                                                                                        ucase["name"]).replace(
                        "${description}", ucase["desc"])
                    file.write(rendered)
                    ucases_created += 1

        print(f"Success create new ucase {folder_name} with {ucases_created} ucase")
        pass
