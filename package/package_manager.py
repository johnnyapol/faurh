"""Begin Imports"""
# Python stdlib imports
import subprocess

"""End Imports"""


class Package:
    def __init__(self, name, description, origin, version):
        self._name = name
        self._description = description
        self._origin = origin
        self._version = version

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_origin(self):
        return self._origin

    def get_version(self):
        return self._version

    def __str__(self):
        return f"{self.get_origin()}/{self.get_name()} (v{self.get_version()}) - {self.get_description()}"

    def __repr__(self):
        return self.__str__()


class PackageManager:
    def __init__(self):
        pass

    def search(self, package_name):
        pass

    def install(self, package_name):
        pass

    def check_for_updates(self):
        pass


def invoke_cmd(args, want_output=False):
    return subprocess.run(
        args, stdout=(subprocess.PIPE if want_output else None), encoding="utf-8"
    ).stdout
