import subprocess
import psutil

from colorama import Fore
from colorama import Style


def cpu_model():
    model = subprocess.getoutput('wmic cpu get name').splitlines()[2].strip()
    cpu_clockspeed = subprocess.getoutput('wmic cpu get maxclockspeed').splitlines()[2].strip()

    return {
         'model': f'CPU Model: {model} @ {cpu_clockspeed}Hz'.strip(),
         'model_raw': len(f'CPU Model: {model} @ {cpu_clockspeed}Hz'.strip())
    }


def cpu_usage():
    cpu_percent = psutil.cpu_percent()
    cpu_usage_bar = '█' * int(cpu_percent / 100.0 * 30) + ' ' * (30 - int(cpu_percent / 100.0 * 30))

    col = {
        cpu_percent < 33: Fore.GREEN,
        33 <= cpu_percent < 66: Fore.YELLOW,
        66 <= cpu_percent: Fore.RED
    }

    return {
        'usage_bar': f"\rCPU Usage:  [" + col[True] + f"{cpu_usage_bar}{Style.RESET_ALL}] " + col[True] + f"{cpu_percent:.2f}%{Style.RESET_ALL}".strip(),
        'usage_raw': 45 + len(f"{cpu_percent:.2f}%".strip()),
        'usage': f'{cpu_percent:.2f}%'
    }
