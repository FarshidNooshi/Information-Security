import os

import nmap
import pyfiglet as pyfiglet

SAVE_DIR = '/results/result_port scan.txt'


def scan_ports(host_addr, start_port_num, last_port_num):
    host_scan = nmap.PortScanner()
    host_scan.scan(host_addr, generate_range(last_port_num, start_port_num))
    curr_path = os.path.dirname(os.path.abspath(__file__))
    with open(curr_path + SAVE_DIR, 'w') as f:
        for host in host_scan.all_hosts():
            print(f"state of the host({host_scan[host]['hostnames'][0]['name']}): {host_scan[host].state()}")
            for protocol in host_scan[host].all_protocols():
                print(f'protocol: {protocol}')
                for port in host_scan[host][protocol].keys():
                    if host_scan[host][protocol][port]['state'] == 'open':
                        save_open_port(port, f, host_scan[host][protocol][port])
                    else:
                        print(
                            f"port: {port}, state: {host_scan[host][protocol][port]['state']},"
                            f" service: {host_scan[host][protocol][port]['name']}")


def generate_range(last_port_num, start_port_num):
    return start_port_num + '-' + last_port_num


def save_open_port(port, f, scan_result):
    print(f"open port: {port}, service: {scan_result['name']}")
    f.write(f"open port: {port}, service: {scan_result['name']}")


if __name__ == '__main__':
    print(pyfiglet.figlet_format('Port Scanner'))
    host = input('Host IP: ')
    start_port = input('Start port: ')
    last_port = input('last port: ')
    scan_ports(host, start_port, last_port)
