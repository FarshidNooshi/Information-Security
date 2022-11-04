import os

import nmap

SAVE_DIR = '/results/result_port scan.txt'


def scan_ports(host_addr, start_port_num, last_port_num):
    host_scan = nmap.PortScanner()
    host_scan.scan(host_addr, generate_range(last_port_num, start_port_num))
    curr_path = os.path.dirname(os.path.abspath(__file__))
    with open(curr_path + SAVE_DIR, 'w') as f:
        for host in host_scan.all_hosts():
            print(f'state of the host: {host_scan[host].state()}')
            for protocol in host_scan[host].all_protocols():
                print(f'protocol: {protocol}')
                for port in host_scan[host][protocol].keys():
                    if host_scan[host][protocol][port]['state'] == 'open':
                        save_open_port(port, f)


def generate_range(last_port_num, start_port_num):
    return start_port_num + '-' + last_port_num


def save_open_port(port, f):
    print(f'open port: {port}')
    f.write(f'open port: {port}\n')


if __name__ == '__main__':
    host = input('Host IP: ')
    start_port = input('Start port: ')
    last_port = input('last port: ')
    scan_ports(host, start_port, last_port)
