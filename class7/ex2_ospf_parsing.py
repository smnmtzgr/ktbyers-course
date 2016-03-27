#!/usr/bin/python

import re

f = open("OSPF_DATA/ospf_single_interface.txt", "r")

ospf_dict = {}

for line in f:
    intf = re.search(r"(.+) is up, line protocol is up", line)
    if intf:
        ospf_dict['Int'] = intf.group(1)

    ip_area = re.search(r"Internet Address (.+), Area (.+?)", line)
    if ip_area:
        ospf_dict['IP'] = ip_area.group(1)
        ospf_dict['Area'] = ip_area.group(2)

    type_cost = re.search(r"Network Type (.+), Cost: (.+)", line)
    if type_cost:
        ospf_dict['Type'] = type_cost.group(1)
        ospf_dict['Cost'] = type_cost.group(2)

    hello_dead = re.search(r"Hello (.+), Dead (.+?)", line)
    if hello_dead:
        ospf_dict['Hello'] = hello_dead.group(1)
        ospf_dict['Dead'] = hello_dead.group(2)

print
field_order = ('Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead')
for k in field_order:
    print "%15s: %-20s" % (k, ospf_dict[k])

print
