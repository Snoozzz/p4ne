from ipaddress import IPv4Network
import random

list_of_network=[]

na = random.randint(0x0B000000, 0xDF000000)
m = random.randint(8, 24)

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, na="0.0.0.0", m="/0"):
        na = random.randint(0x0B000000, 0xDF000000)
        m = random.randint(8, 24)
        IPv4Network.__init__(self, (na, m), strict=False)
        #self.subnets = na
    def key_value(self):
        a = int(self.network_address._ip)
        b = int(self.netmask._ip)
        return a+b*2**32

def nsort(x):
    return(x.key_value())


for i in range(0, 50):
    list_of_network.append(IPv4RandomNetwork())
l = sorted(list_of_network, key=nsort)
print(l)
