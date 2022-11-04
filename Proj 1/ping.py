import os
from time import sleep

from ping3 import verbose_ping

SAVE_DIR = '/results/result_ping.txt'


def ping_server(server: str):
    """ping server"""
    return verbose_ping(server)


if __name__ == '__main__':
    while True:
        addr = input('IP/Domain: ')
        out = ping_server(addr)
        sleep(3)
