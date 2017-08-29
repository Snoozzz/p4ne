import glob
import ipaddress
import re



list_n=[]
rlist = glob.glob(('C:\\Users\\A.Meshkov\\Seafile\\p4ne_training\\config_files\\*.txt'))


def class_ip(x):
    a = re.match(r'^ ip address ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+) ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1) + '/' + a.group(2)), 0)
    a = re.match(r'^ gateway ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1)), 10)
    a = re.match(r'^ standby [0-9]+? ip ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1)), 5)
    a = re.match(r'route 0\.0\.0\.0 0\.0\.0\.0 ([0-9]+[.][0-9]+[.][0-9]+[.][0-9]+)', x)
    if a:
        return (ipaddress.IPv4Interface(a.group(1)), 10)
    return None

# for name in rlist:
#     with open(name) as f:
#         str_list = list(f)
#         for str in str_list:
#             p = class_ip(str)
#             print(p)

    if __name__ == '__main__':

        set_of_ip = set()

        for current_file_name in glob.glob("/Users/mk/Seafile/p4ne_training/config_files/*.txt"):
            with open(current_file_name) as f:
                for current_line in f:
                    addr = class_ip(current_line)
                    if addr:
                        set_of_ip.add(addr)

        addr_plan = {}
        hosts = []

        # Fill addr_plan with subnets
        for ip_addr in set_of_ip:
            if ip_addr[0].network.prefixlen != 32:  # Subnets
                subnet_key = str(ip_addr[0].network)
                if subnet_key not in addr_plan.keys():
                    addr_plan[subnet_key] = [(str(ip_addr[0].ip), ip_addr[1])]
                else:
                    addr_plan[subnet_key].append((str(ip_addr[0].ip), ip_addr[1]))
            else:  # Hosts
                hosts.append((ip_addr[0].ip, ip_addr[1]))

        # Add gateways to addr_plan
        for subnet_key in addr_plan.keys():
            for gw in hosts:
                if gw[0] in ipaddress.IPv4Network(subnet_key):
                    addr_plan[subnet_key].append((str(gw[0]), gw[1]))

print(addr_plan)




#print(sorted(list(set(list_n))))