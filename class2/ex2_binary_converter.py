ip_addr = raw_input("Please enter ip-address: ")

octets = ip_addr.split('.')

first_octet_bin = bin(int(octets[0]))
second_octet_bin = bin(int(octets[1]))
third_octet_bin = bin(int(octets[2]))
fourth_octet_bin = bin(int(octets[3]))

print "\n\n"
print "%10s %10s %10s %10s" % ("first_octet", "second_octet", "third_octet",
                               "fourth_octet")
print "%10s %10s %10s %10s" % (first_octet_bin, second_octet_bin,
                               third_octet_bin, fourth_octet_bin)
print "\n\n"
