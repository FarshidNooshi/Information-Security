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


if __name__ == '__main__':
    while True:
        addr = input('Please Enter Your IP/Domain: ')
        begin_port = input('Please Enter Your starting port number: ')
        end_port = input('Please Enter Your ending port number: ')
        scan_ports(addr, begin_port, end_port)
        sleep(3)
