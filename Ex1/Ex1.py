import re
import socket
import struct

#pattern matching for ip address
while 1:
    ip_addr = raw_input("Enter Ip address: ")
    ip = re.match(r"^(?=.*[^\.]$)((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.?){4}$", ip_addr)
    if ip != None:
        break
    print("Invalid IP address format")

#create binary ip
bin_ip = []
my_ip = ip.group(0)
addr = my_ip.split(".")#get rid of the dots(.)
for ips in addr:
    ibin = bin(int(ips))[2:].zfill(8)
    bin_ip.append(ibin)


#pattern matching for nm in dec format
while 1:
    nm_addr = raw_input("Enter subnet mask in decimal format: ")
    nm = re.match(r"^(?=.*[^\.]$)(\/)([3][0-2]|[1-2][0-9]|[0-9])$", nm_addr)
    if nm != None:
        break
    print("Subnet mask is invalid")


my_nm = nm.group(0)
my_nm = my_nm.split("/")
cidr = int(my_nm[1])
#https://gist.github.com/nboubakr/4344773
# Initialize the netmask and calculate based on CIDR mask
mask = [0, 0, 0, 0]
for i in range(cidr):
	mask[i/8] = mask[i/8] + (1 << (7 - i % 8))

# Initialize net and binary and netmask with addr to get network
net = []
for i in range(4):
	net.append(int(addr[i]) & mask[i])

# Duplicate net into broad array, gather host bits, and generate broadcast
broad = list(net)
brange = 32 - cidr
for i in range(brange):
	broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))

# Print information, mapping integer lists to strings for easy printing
for line in [addr, bin_ip]:
    print('{:>8} {:>8} {:>8}'.format(*line))
print "\n"
print "network address is: " , ".".join(map(str, net))
print "broadcast address is:" , ".".join(map(str, broad))
