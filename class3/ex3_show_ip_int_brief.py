import pprint

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''
show_ip_lines = show_ip_int_brief.split('\n')

tuple_list = []

for line in show_ip_lines:
    if 'Interface' in line:
        continue
    line_splitted = line.split()

    if len(line_splitted) == 6:
        if line_splitted[4] == 'up' and line_splitted[5] == 'up':
            tuple_list.append((line_splitted[0],line_splitted[1],line_splitted[4],line_splitted[5]))

pprint.pprint(tuple_list)
