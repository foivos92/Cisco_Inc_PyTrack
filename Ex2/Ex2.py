import re
#we need one set for the unique vlans -> unique_vlans
#one for all the common vlans -> all_common
#one for every vlan we ve seen  -> all_sofar
#and a temp -> vlan_list
unique_vlans = set()
all_common = set()
vlan_list = []
all_sofar= set()
f=open("commands.txt","r")
j = 1
# read each line
for line in f:
    match = None
    match = re.match(r"^(?=.*[^\.]$)(switchport trunk allowed vlan ((\d)(,\d+)*|(\d)))$", str(line))
    #every line that we need to look
    if match != None:
        vlan_list = match.group(2).split(",")
        vlan_set = set(vlan_list)
        #fill in the sets if its the 1st time you read a line
        if j == 1:
            all_sofar = vlan_set
            all_common = vlan_set
            unique_vlans = vlan_set
            j = 0
            continue
        #update the sets
        #new all_common is the common between the old
        #all_common and the one we just got
        all_common = all_common & vlan_set
        #new unique_vlans are the ones that are unique between the old unique_vlans and vlan_set
        #and the ones that we have never seen before
        unique_vlans = unique_vlans - vlan_set | vlan_set - all_sofar
        #we update all_sofar
        all_sofar = all_sofar | vlan_set

#format and printing        
L1 = list(sorted(all_common, key = int))
L2 = list(sorted(unique_vlans, key = int))
print ("List_1="+'[%s]' % ', '.join(map(str, L1)))
print ("List_2="+'[%s]' % ', '.join(map(str, L2)))
