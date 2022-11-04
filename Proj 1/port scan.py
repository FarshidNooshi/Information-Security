# https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap
import nmap


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


if __name__ == '__main__':
    scan_ports()
