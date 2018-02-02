import re

proto_dict = {"O":"OSPF","D":"EIRGP","R":"RIP","B":"BGP","E":"EGP","i":"IS-IS","o":"ODR","H":"NHRP","l":"LISP"}
f=open("ShowIpRoute.txt","r")
for line in f:
    match = None
    match = re.match(r"^(?=.*[^\.]$)((O|D|R|B|E|i|o|H|l)( (..))? (.+) \[(.+)\] via (.+), (.+), (.+))$", str(line))
    if match != None:
        print "{0:<21}{1:<21}".format("Protocol:",proto_dict[str(match.group(2))])
        print "{0:<21}{1:<21}".format("Prefix:",str(match.group(5)))
        print "{0:<21}{1:<21}".format("AD/Metric:",str(match.group(6)))
        print "{0:<21}{1:<21}".format("Next-Hop:",str(match.group(7)))
        print "{0:<21}{1:<21}".format("Last Update:",str(match.group(8)))
        print "{0:<21}{1:<21}".format("Outbound Interface:",str(match.group(9)))
