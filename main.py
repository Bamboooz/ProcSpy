import os
import time

from prompt.prompt import draw_proc_spy_screen


if __name__ == '__main__':
    os.system('color')

    while True:
        print("\033[2J\033[1;1H", end="")
        print(draw_proc_spy_screen())
        time.sleep(0.5)
