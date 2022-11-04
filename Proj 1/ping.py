from time import sleep

from ping3 import verbose_ping


def ping_server(server: str):
    """ping server"""
    return verbose_ping(server)


if __name__ == '__main__':
    while True:
        addr = input('Please Enter Your IP/Domain: ')
        out = ping_server(addr)
        print(out)
        sleep(3)
