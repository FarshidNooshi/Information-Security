import os

import nmap


def scan_ip():
    address = input('Enter the Network Address: ')
    subnet = input('Enter the subnet: ')
    host = nmap.PortScannerYield()
    progressive_results = host.scan(hosts=address + '/' + subnet, arguments="-sn")
    curr_path = os.path.dirname(os.path.abspath(__file__))
    with open(curr_path + '/results/ip_scan.txt', 'w') as f:
        for result in progressive_results:
            save_result(result, f)


def save_result(result, f):
    print(f'{result[0]}: UP')
    f.write(f'{result[0]}: UP\n')


if __name__ == '__main__':
    scan_ip()
