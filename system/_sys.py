import platform
import time

import psutil


def sys_version():
    return platform.platform()


def machine_name():
    return platform.node()


def os_uptime():
    return str(round((time.time() - psutil.boot_time()) / 60 / 60, 2)) + 'h'
