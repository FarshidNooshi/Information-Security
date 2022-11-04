from time import sleep

import nmap


def generate_port(start, last):
    return start + '-' + last


def scan_ports(host, start, last):
    nm = nmap.PortScanner()
    nm.scan(host, generate_port(start, last))
    # print(nm.command_line())
    with open('result_port.txt', 'w') as f:
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            list(lport).sort()
            for port in lport:
                port_status = nm[host][proto][port]['state']
                if port_status == 'open':
                    item = "Port Open:-->\t{}".format(str(port))
                    f.write(item + '\n')
                    print(item)


import socket


def isOpen(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.1)
    result = sock.connect_ex((hostname, port))
    sock.close()
    return result == 0


def ipScan(host, start, end):
    live_hosts = []
    for i in range(start, end):
        tmp_host = host + '.' + str(i)
        res = isOpen(tmp_host, 23)
        if res:
            yield tmp_host


for host in ipScan('89.43.3', 1, 255):
    print(host)

# if __name__ == '__main__':
#     while True:
#         addr = input('Please Enter Your IP/Domain: ')
#         begin_port = input('Please Enter Your starting port number: ')
#         end_port = input('Please Enter Your ending port number: ')
#         scan_ports(addr, begin_port, end_port)
#         sleep(3)
