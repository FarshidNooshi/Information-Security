import os
from time import sleep

from ping3 import verbose_ping

SAVE_DIR = '/results/ping.txt'


def ping_server(server: str):
    """ping server"""
    return verbose_ping(server)


if __name__ == '__main__':
    while True:
        addr = input('Please Enter Your IP/Domain: ')
        out = ping_server(addr)
        # curr_path = os.path.dirname(os.path.abspath(__file__))
        # with open(curr_path + SAVE_DIR, 'w') as f:
        #     f.write(f'{addr}\n: {out}')
        sleep(3)
