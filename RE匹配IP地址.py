import re
str1 = 'Port-channel1.189   192.168.1.189  YES   CONFIG   up'
result = re.match('\s*(.*\.\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(YES|NO)\s+(CONFIG|DHCP)\s+(up|down)\s*',str1).groups()
print('-'*100)
print('%-10s : %s' %('接口',result[0]))
print('%-10s : %s' %('IP地址',result[1]))
print('%-10s : %s' %('状态',result[4]))


