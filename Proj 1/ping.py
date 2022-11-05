import os
from time import sleep

import pyfiglet

SAVE_DIR = '/results/result_ping.txt'
NUMBERS_OF_PINGS = 4

if __name__ == '__main__':
    print(pyfiglet.figlet_format('Ping checker'))
    while True:
        addr = input('IP/Domain: ')
        out = os.system(f'ping {addr} -t {NUMBERS_OF_PINGS}')
        sleep(3)
