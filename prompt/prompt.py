from system._inet import *
from sensor._cpu import *
from sensor._mem import *
from system._sys import *
from system._time import *
from system._fs import *
from sensor._proc import *

PROC_SPY_VER = '1.0.0'


def draw_proc_spy_screen():
    # calls it once as variable instead of calling it everywhere, because sensors ar being overloaded
    cpu_models = cpu_model()
    cpu_usages = cpu_usage()
    mem_usages = memory_usage()
    swap_usages = swap_usage()

    inline_memory_bar = set_inline_spaces(cpu_models['model_raw'], cpu_usages['usage_raw'], mem_usages['usage_raw'], swap_usages['usage_raw'])
    inline_swap_bar = set_inline_spaces(len(mem_usages['usage']), len(mem_usages['usage_total']), len(mem_usages['usage_used']), len(mem_usages['usage_free']))
    inline_connection_bar = set_inline_spaces(len(f'Connected:{is_connected()}'), len('NETWORK                         State'))[0]
    inline_ping_bar = set_inline_spaces(len(f'Ping time:{get_ping_time(True)}'), len('NETWORK                         State'))[0]

    proc_spy_screen = f'''(ProcSpy v.{PROC_SPY_VER}) - ({machine_name()}) - ({sys_version()}) - (IP: {get_ipv4()}) - (Uptime: {os_uptime()})
    
{cpu_models['model']}{inline_memory_bar[0]}      MEM:   {mem_usages['usage_col']}{inline_swap_bar[0]}      SWAP:  {swap_usages['usage_col']}
    {cpu_usages['usage_bar']}{inline_memory_bar[1]}      total: {mem_usages['usage_total']}{inline_swap_bar[1]}      total: {swap_usages['usage_total']}
    {mem_usages['usage_bar']}{inline_memory_bar[2]}      used:  {mem_usages['usage_used']}{inline_swap_bar[2]}      used:  {swap_usages['usage_used']}
    {swap_usages['usage_bar']}{inline_memory_bar[3]}      free:  {mem_usages['usage_free']}{inline_swap_bar[3]}      free:  {swap_usages['usage_free']}

NETWORK                         State        TASKS {get_task_number()} ({get_threads()} threads), {get_running_tasks()} running, {get_sleeping_tasks()} sleeping
Connected:{inline_connection_bar}{is_connected(True)}
Ping time:{inline_ping_bar}{get_ping_time()}

FILE SYS                 Used   Total
{get_file_system_info()}
{time()} {get_timezone()}
    '''

    return proc_spy_screen
