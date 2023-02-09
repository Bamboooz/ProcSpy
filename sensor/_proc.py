import subprocess

import psutil


def get_task_number():
    proc = subprocess.getoutput('tasklist').splitlines()[3:]
    return len(proc)


def get_threads():
    return


def get_running_tasks():
    return


def get_sleeping_tasks():
    return


print(psutil.users())
