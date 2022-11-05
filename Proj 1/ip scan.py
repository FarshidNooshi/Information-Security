import os

import nmap
import pyfiglet

ARGUMENTS = "-sn"
SAVE_DIR = '/results/result_ip scan.txt'


def scan_ip():
    address = input('Address: ')
    subnet = input('Subnet: ')
    host = nmap.PortScannerYield()
    progressive_results = host.scan(hosts=generate_address(address, subnet), arguments=ARGUMENTS)
    curr_path = os.path.dirname(os.path.abspath(__file__))
    results_count = 0
    with open(curr_path + SAVE_DIR, 'w') as f:
        for result in progressive_results:
            save_result(result, f)
            results_count += 1
        print(f"Scan results saved to {curr_path + SAVE_DIR}\n"
              f"Total number of results: {results_count}")


def generate_address(address, subnet):
    return address + '/' + subnet


def save_result(result, f):
    print(f'{result[0]}: UP')
    f.write(f'{result[0]}: UP\n')


if __name__ == '__main__':
    print(pyfiglet.figlet_format('IP Scanner'))
    scan_ip()
