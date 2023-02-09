import os
import psutil
import re

from colorama import Fore, Style
from scripts._common import set_inline_spaces


def get_file_system_info():
    fs_data = ''''''

    for fs in get_file_systems():
        fs_data += fs
        fs_data += set_inline_spaces(len(fs), len('FILE SYS                 '))[0]
        fs_data += f"{Fore.BLUE}{get_used_space(fs)}{Style.RESET_ALL}"
        fs_data += set_inline_spaces(len(get_used_space(fs)), len('Used   '))[0]
        fs_data += f"{Fore.BLUE}{get_total_space(fs)}{Style.RESET_ALL}"
        fs_data += '\n'

    return fs_data


def get_file_systems():
    return re.findall(r"[A-Z]+:.*$", os.popen("mountvol /").read(), re.MULTILINE)


def get_total_space(drive_letter):
    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.total / (1024.0 ** 3))) + 'GB'


def get_used_space(drive_letter):
    obj_disk = psutil.disk_usage(drive_letter)
    return str(round(obj_disk.used / (1024.0 ** 3))) + 'GB'
