from ipaddress import IPv4Network
import random

#random.randint(0,100)
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
        int(self.network_address._ip)
        int(self.netmask._ip)
        return(self)

def c():



for i in range(0, 50):
    list_of_network.append(IPv4RandomNetwork())

  #  sorted(list_of_network, key=)

print(list_of_network)
