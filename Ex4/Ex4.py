access_template = ['switchport mode access','switchport access vlan {}','switchport nonegotiate','spanning-tree portfast','spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q','switchport mode trunk','switchport trunk allowed vlan {}']


mode = raw_input("Enter interface mode(access/trunk): ")
inter = raw_input("Enter interface type and number: ")
if mode == "access":
    vlan = raw_input("Enter VLAN number: ")
    access_template[1] = access_template[1].replace("{}",str(vlan))
    print "Interface ", inter
    print "\n".join(access_template)
elif mode == "trunk":
    vlan = raw_input("Enter allowed VLANs: ")
    trunk_template[2] = trunk_template[2].replace("{}",str(vlan))
    print "Interface ", inter
    print "\n".join(trunk_template)
else:
    print ("wrong interface mode")
