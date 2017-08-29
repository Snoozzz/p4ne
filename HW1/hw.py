import glob
import ipaddress
import re



list_n=[]
rlist = glob.glob(('C:\\Users\\A.Meshkov\\Seafile\\p4ne_training\\config_files\\*.txt'))


def class_ip(x):
    a = re.match(r'^ ip address ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+) ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1) + '/' + a.group(2)), 0)
    a = re.match(r'^ ip default-gateway ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1)), 10)
    a = re.match(r'^ standby [0-9]+? ip ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1)), 5)
    a = re.match(r'ip route 0\.0\.0\.0 0\.0\.0\.0 ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1)), 10)
    return None

for name in rlist:
    with open(name) as f:
        str_list = list(f)
        for str in str_list:
            p = class_ip(str)
            print(p)

#print(sorted(list(set(list_n))))