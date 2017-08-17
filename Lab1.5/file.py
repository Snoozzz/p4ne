import glob
import os

#os.PathLike=('C:\\Users\\A.Meshkov\\Seafile\\p4ne_training\\config_files\\*.txt')
list_n=[]
rlist = glob.glob(('C:\\Users\\A.Meshkov\\Seafile\\p4ne_training\\config_files\\*.txt'))

for name in rlist:
    with open(name) as f:
        str_list = list(f)
        for str in str_list:
            if str.find('ip address ')>0:
                list_n.append(str.replace('ip address ', '').strip())


print(sorted(list(set(list_n))))



# l = sorted(list(set(list(open(’test.csv')))))
#print(l)
