import datetime


def time():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def get_timezone():
    now = datetime.datetime.now()
    local_now = now.astimezone()
    return local_now.tzinfo
