#/usr/bin/env python3

import subprocess
import ipaddress
import sys
from subprocess import Popen, PIPE

network_scan = ipaddress.ip_network(sys.argv[1])
free_ip = []

for i in network_scan.hosts():
    i = str(i)
    ping_ping = Popen(['ping', '-c', '2', i], stdout=PIPE)
    output = ping_ping.communicate()[0]
    hostalive = ping_ping.returncode

    if hostalive == 0:
        print (i, "Reachable")
    else:
        print (i, "Unreachable")
        free_ip.append([i])

print ("The number of the free IP is", len(free_ip))
print (free_ip)
