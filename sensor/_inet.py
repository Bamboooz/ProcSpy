import socket


def get_ipv4():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)
