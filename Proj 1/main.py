import socket
import subprocess
import sys
from time import sleep

import nmap
from ping3 import verbose_ping


def scan_ip():
    address = input('Enter the Network Address: ')
    subnet = input('Enter the subnet: ')
    host = nmap.PortScannerYield()
    print("scanning in progress...\n")
    for progressive_result in host.scan(hosts=address + '/' + subnet, arguments="-sn"):
        if int(progressive_result[1]["nmap"]["scanstats"]["uphosts"]):
            print(f'{progressive_result[0]} ---> Live\n')


# https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
def scan_ports():
    host = input('Enter the remote host IP to scan: ')
    start_port = input('Enter the Start port number:\t')
    last_port = input('Enter the last port number:\t')
    host_scan = nmap.PortScanner()
    host_scan.scan(host, start_port + '-' + last_port)
    for host in host_scan.all_hosts():
        print('Host : %s (%s)' % (host, host_scan[host].hostname()))
        print('State : %s' % host_scan[host].state())
        for proto in host_scan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = host_scan[host][proto].keys()
            for port in lport:
                if host_scan[host][proto][port]['state'] == "open":
                    print('Port Open:-->\t %s ' % port)


def ping_server(server: str):
    """ping server"""
    return verbose_ping(server)


if __name__ == '__main__':
    while True:
        inp = input('\nPlease enter mode:\n'
                    '1- Ping\n'
                    '2- Scan ip\n'
                    '3- Scan ports\n'
                    '4- Exit\n')
        if inp == "1":
            ping_ip = input('Please Enter Your IP/Domain: ')
            out = ping_server(ping_ip)
            print(out)
            sleep(5)
        elif inp == "2":
            scan_ip()
        elif inp == "3":
            scan_ports()
        elif inp == "4":
            sys.exit(0)
        else:
            print("Wrong input.")
