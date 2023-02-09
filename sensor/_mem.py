import psutil

from colorama import Fore, Style, Back


def memory_usage():
    mem_percent = psutil.virtual_memory()
    mem_usage_bar = '|' * int(mem_percent.percent / 100.0 * 30) + ' ' * (30 - int(mem_percent.percent / 100.0 * 30))

    fore_col = {
        mem_percent.percent < 33: Fore.GREEN,
        33 <= mem_percent.percent < 66: Fore.YELLOW,
        66 <= mem_percent.percent: Fore.RED
    }

    back_col = {
        mem_percent.percent < 33: Back.GREEN,
        33 <= mem_percent.percent < 66: Back.YELLOW,
        66 <= mem_percent.percent: Back.RED
    }

    return {
        'usage_bar': f"\rMEM Usage:  [" + fore_col[True] + f"{mem_usage_bar}{Style.RESET_ALL}] " + fore_col[True] + f"{mem_percent.percent:.2f}%{Style.RESET_ALL}".strip(),
        'usage_raw': 45 + len(f"{mem_percent.percent:.2f}%".strip()),
        'usage': f'{mem_percent.percent:.2f}%',
        'usage_col': back_col[True] + f'{mem_percent.percent:.2f}%{Style.RESET_ALL}',
        'usage_total': str(round(mem_percent.total / 1024**3, 2)) + 'GB',
        'usage_used': str(round(mem_percent.used / 1024**3, 2)) + 'GB',
        'usage_free': str(round(mem_percent.free / 1024**3, 2)) + 'GB'
    }


def swap_usage():
    swap_percent = psutil.swap_memory()
    swap_usage_bar = '|' * int(swap_percent.percent / 100.0 * 30) + ' ' * (30 - int(swap_percent.percent / 100.0 * 30))

    fore_col = {
        swap_percent.percent < 33: Fore.GREEN,
        33 <= swap_percent.percent < 66: Fore.YELLOW,
        66 <= swap_percent.percent: Fore.RED
    }

    back_col = {
        swap_percent.percent < 33: Back.GREEN,
        33 <= swap_percent.percent < 66: Back.YELLOW,
        66 <= swap_percent.percent: Back.RED
    }

    return {
        'usage_bar': f"\rSWAP Usage: [" + fore_col[True] + f"{swap_usage_bar}{Style.RESET_ALL}] " + fore_col[True] + f"{swap_percent.percent:.2f}%{Style.RESET_ALL}".strip(),
        'usage_raw': 45 + len(f"{swap_percent.percent:.2f}%".strip()),
        'usage': f'{swap_percent.percent:.2f}%',
        'usage_col': back_col[True] + f'{swap_percent.percent:.2f}%{Style.RESET_ALL}',
        'usage_total': str(round(swap_percent.total / 1024 ** 3, 2)) + 'GB',
        'usage_used': str(round(swap_percent.used / 1024 ** 3, 2)) + 'GB',
        'usage_free': str(round(swap_percent.free / 1024 ** 3, 2)) + 'GB'
    }
