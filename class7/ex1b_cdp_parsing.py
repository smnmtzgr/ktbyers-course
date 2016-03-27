#!/usr/bin/python

import re

f = open("CDP_DATA/sw1_cdp.txt", "r")
cdp_data = f.read()
f.close()

tmp_dict = {}

tmp_dict['remote_hosts'] = re.findall(r"Device ID: (.+)", cdp_data)
tmp_dict['IPs'] = re.findall(r"IP address: (.+)", cdp_data)
tmp_dict['platform'] = re.findall(r"Platform: (.+?),", cdp_data)

# Print output
print
field_order = ('remote_hosts', 'IPs', 'platform')
for k in field_order:
    print "%15s: %-20s" % (k, tmp_dict[k])

print
