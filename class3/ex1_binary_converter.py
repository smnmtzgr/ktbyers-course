#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    sys.exit("Usage: %s <ip_address>" % sys.argv[0])

ip_addr = sys.argv.pop()
ip_addr_bin = []

octets = ip_addr.split('.')

if len(octets) == 4:
    for octet in octets:
        bin_octet = bin(int(octet))
        bin_octet = bin_octet[2:]

        while True:
            if len(bin_octet) >= 8:
                break
            bin_octet = '0' + bin_octet

        ip_addr_bin.append(bin_octet)

    ip_addr_bin = ".".join(ip_addr_bin)

    print "\n%-15s %-45s" % ("IP address", "Binary")
    print "%-15s %-45s\n\n" % (ip_addr, ip_addr_bin)

else:
    sys.exit("Invalid IP address entered.")
