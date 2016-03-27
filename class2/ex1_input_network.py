ip_network = raw_input("\n\nPlease enter /24-network: ")

octets = ip_network.split('.')
octets = octets[:3]
octets.append('0')

network = ".".join(octets)

print "Your network is: %s" % network

first_octet_bin = bin(int(octets[0]))
first_octet_hex = hex(int(octets[0]))

print "\n\n"
print "%20s %20s %20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "%20s %20s %20s" % (network, first_octet_bin, first_octet_hex)
print "\n\n"
