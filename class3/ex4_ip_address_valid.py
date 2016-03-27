#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
        ip_addr = sys.argv.pop()
else:
    sys.exit("Usage: %s <ip_address>" % sys.argv[0])

octets = ip_addr.split('.')

if len(octets) != 4:
    sys.exit("\n\n Invalid ip address %s\n" % ip_addr)

valid_ip = True

for i,octet in enumerate(octets):
    try:
        octets[i] = int(octet)
    except ValueError:
        sys.exit("\n\nInvalid IP address: %s\n" % ip_addr)

first_octet, second_octet, third_octet, fourth_octet = octets

if first_octet < 1:
    valid_ip = False
elif first_octet > 223:
    valid_ip = False
elif first_octet == 127:
    valid_ip = False

if first_octet == 169 and second_octet == 254:
    valid_ip = False

for octet in (second_octet, third_octet, fourth_octet):
    if (octet < 0) or (octet > 255):
        valid_ip = False

if valid_ip:
    print "\n\nThe ip address %s is valid\n" % ip_addr
else:
    print "\n\nThe ip address %s is invalid\n" % ip_addr
