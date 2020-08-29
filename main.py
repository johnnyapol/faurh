#!/usr/bin/env python3
"""Begin Imports"""
# Internal imports
from package.aur_manager import AURManager
from package.pacman_wrapper import PacmanWrapper
from package.fwupd_wrapper import FirmwareUpdateWrapper

# Python stdlib imports
from argparse import ArgumentParser

"""End Imports"""


def parse_args():
    args = ArgumentParser(prog="faurh", description="faurh - the Friendly AUR Helper")
    return args.parse_args()


def do_normal_execution():
    interfaces = [PacmanWrapper(), AURManager(), FirmwareUpdateWrapper()]

    for interface in interfaces:
        interface.check_for_updates()


def main(args):
    do_normal_execution()


if __name__ == "__main__":
    main(parse_args())
