"""Begin Imports"""
# Internal imports
from package.package_manager import PackageManager
from package.package_manager import Package
from package.pacman_wrapper import invoke_pacman

# Python stdlib imports
import requests

"""End Imports"""


def send_aur_rpc(arguments):
    aur_req = requests.get(f"https://aur.archlinux.org/rpc/?v=5{arguments}")
    return (aur_req.status_code, aur_req.json())


def do_aur_search(package_name):
    return send_aur_rpc(f"&type=search&arg={package_name}")


def do_aur_lookup(package_names):
    return send_aur_rpc(
        f"&type=info{''.join(f'&arg[]={pkg}' for pkg in package_names)}"
    )


def generate_aur_packages(aur_data):
    if aur_data[0] != 200:
        return None
    aur_json = aur_data[1]["results"]

    return (
        Package(pkg_json["Name"], pkg_json["Description"], "aur", pkg_json["Version"])
        for pkg_json in aur_json
    )


class AURManager(PackageManager):
    def __init__(self):
        super().__init__()

    def search(self, package_name):
        return generate_aur_packages(do_aur_search(package_name))

    def lookup(self, package_names):
        return generate_aur_packages(do_aur_lookup(package_names))

    def install(self, package_name):
        pass

    def check_for_updates(self):
        print("Checking for updates to AUR packages...")

        package_data = invoke_pacman(["-Qm"], want_output=True)
        package_splits = (line.split(" ") for line in package_data.splitlines())
        packages = dict((split[0], split[1]) for split in package_splits)
        aur_packages = self.lookup(pkg for pkg in packages)

        for pkg in aur_packages:
            local_ver = packages[pkg.get_name()]
            if local_ver != pkg.get_version():
                # Update available
                print("Update for " + pkg.get_name())
            del packages[pkg.get_name()]

        # Non-AUR packs remain in the package dictionary
