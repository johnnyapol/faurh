"""Begin Imports"""
# Internal imports
from package.package_manager import PackageManager
from package.package_manager import invoke_cmd


class FirmwareUpdateWrapper(PackageManager):
    def __init__(self):
        super().__init__()

    def check_for_updates(self):
        print("Checking for firmware updates...")
        invoke_cmd(["fwupdmgr", "refresh"], want_output=False)  # discard
        invoke_cmd(["fwupdmgr", "update"])
