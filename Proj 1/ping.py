import os
from time import sleep

SAVE_DIR = '/results/result_ping.txt'

if __name__ == '__main__':
    while True:
        addr = input('IP/Domain: ')
        out = os.system(f'ping {addr} -t 4')
        sleep(3)
