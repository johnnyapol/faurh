"""Begin Imports"""
# Internal imports
from package.package_manager import PackageManager
from package.package_manager import invoke_cmd

"""End Imports"""


def invoke_pacman(args, want_output=False, need_root=False):
    process_args = []
    if need_root:
        process_args.append("sudo")
    process_args.append("pacman")
    process_args.extend(args)

    return invoke_cmd(process_args, want_output)


class PacmanWrapper(PackageManager):
    def __init__(self):
        super().__init__()

    def search(self, package_name):
        pass

    def install(self, package_name):
        pass

    def check_for_updates(self):
        print("Checking for updates in pacman repositories...")
        invoke_pacman(["-Syu"], need_root=True)
