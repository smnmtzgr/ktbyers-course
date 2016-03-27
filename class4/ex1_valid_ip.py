#!/usr/bin/env python

import sys

not_done = True
while not_done:

    valid_ip = True

    ip_addr = raw_input("\n\nPlease enter an IP address: ")

    octets = ip_addr.split('.')

    if len(octets) != 4:
        print "\nOoops, you don't have 4 octets - try again."
        continue

    for i,octet in enumerate(octets):
        try:
            octets[i] = int(octet)
        except ValueError:
            valid_ip = False

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
        not_done = False
    else:
        print "\n\nThe ip address %s is invalid\n" % ip_addr

print "\n\nThe IP address is valid: %s\n" % ip_addr
