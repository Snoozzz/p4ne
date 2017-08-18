import glob
import re



#int, host, unclassified

list_n=[]
rlist = glob.glob(('C:\\Users\\A.Meshkov\\Seafile\\p4ne_training\\config_files\\*.txt'))

def class_ip(x):

    a = re.match("^ ip address ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", x)
    if a:
        return ("IP", a.group(1), a.group(2))

    a = re.match("^interface (.+)", x)
    if a:
        return ("INT", a.group(1))

    a = re.match("^hostname (.+)", x)
    if a:
        return ("HOST", a.group(1))

    return ("UNCLASSIFIED",)

for name in rlist:
    with open(name) as f:
        str_list = list(f)
        for str in str_list:
            p = class_ip(str)
            if p[0] !="UNCLASSIFIED":
                print(p)



