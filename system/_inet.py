import speedtest, socket

from colorama import Fore, Style


def get_ipv4():
    if is_connected():
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    else:
        return '...'


def is_connected(formated=False):
    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))

        if formated:
            return f"{Fore.GREEN}True{Style.RESET_ALL}"
        else:
            return True
    except socket.error:
        if formated:
            return f"{Fore.RED}True{Style.RESET_ALL}"
        else:
            return False


def get_ping_time(raw=False):
    if is_connected():
        st = speedtest.Speedtest()
        st.get_servers([])

        ping = str(st.results.ping) + 'ms'

        if raw:
            return ping
        else:
            if st.results.ping <= 60:
                return f"{Fore.GREEN}{str(st.results.ping) + 'ms'}{Style.RESET_ALL}"
            elif 60 < st.results.ping <= 150:
                return f"{Fore.YELLOW}{str(st.results.ping) + 'ms'}{Style.RESET_ALL}"
            else:
                return f"{Fore.RED}{str(st.results.ping) + 'ms'}{Style.RESET_ALL}"
    else:
        return '...'
