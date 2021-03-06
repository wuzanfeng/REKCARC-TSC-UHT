import matplotlib.pyplot as plt
import numpy as np

# data = '''0.00854s | 0.03399s | 0.13942s | 0.65621s |
# 0.00422s | 0.01728s | 0.06795s | 0.29894s |
# 0.00302s | 0.01205s | 0.04818s | 0.19448s |
# 0.00247s | 0.00908s | 0.03776s | 0.15100s |
# 0.00223s | 0.00788s | 0.03150s | 0.12579s |
# 0.00211s | 0.00728s | 0.02834s | 0.11284s |
# 0.00206s | 0.00700s | 0.02673s | 0.10631s |
# 0.00190s | 0.00699s | 0.02403s | 0.10599s |
# 0.00204s | 0.00657s | 0.02682s | 0.08540s |
# 0.00205s | 0.00668s | 0.02459s | 0.09724s |
# 0.00170s | 0.00590s | 0.02163s | 0.07809s |
# 0.00162s | 0.00520s | 0.02050s | 0.07308s |
# 0.00170s | 0.00484s | 0.01808s | 0.06524s |
# 0.00125s | 0.00459s | 0.01531s | 0.05890s |
# 0.00114s | 0.00394s | 0.01380s | 0.05368s |'''
# data = '''0.04101s | 0.16158s | 0.65047s | 2.68258s |
# 0.04319s | 0.15372s | 0.59899s | 2.36608s |
# 0.03149s | 0.10811s | 0.44896s | 1.68811s |
# 0.02759s | 0.09536s | 0.32899s | 1.31387s |
# 0.02540s | 0.09263s | 0.30892s | 1.04187s |
# 0.02378s | 0.08665s | 0.23575s | 0.89775s |
# 0.02327s | 0.08849s | 0.31522s | 0.72554s |
# 0.02297s | 0.08393s | 0.31131s | 0.68641s |
# 0.02305s | 0.08256s | 0.33165s | 0.67264s |
# 0.02351s | 0.08366s | 0.31419s | 0.67175s |
# 0.02503s | 0.08926s | 0.31526s | 1.21293s |
# 0.02523s | 0.08426s | 0.32665s | 1.21559s |
# 0.02560s | 0.08943s | 0.31148s | 1.25053s |
# 0.02554s | 0.08869s | 0.32243s | 1.23589s |
# 0.02619s | 0.08890s | 0.31714s | 1.20727s |'''
# data = '''0.00998s | 0.03824s | 0.16265s | 0.71438s |
# 0.00298s | 0.01066s | 0.04209s | 0.17797s |
# 0.00221s | 0.00725s | 0.02752s | 0.09978s |
# 0.00192s | 0.00556s | 0.02050s | 0.07388s |'''
data = '''0.04069s | 0.16151s | 0.64825s | 2.66666s | 
0.02576s | 0.08296s | 0.31809s | 1.24863s | 
0.02205s | 0.04532s | 0.16570s | 0.63102s | 
0.02364s | 0.08014s | 0.14077s | 0.52902s |'''

data = list(map(float, data.split('s |')[:-1]))
# th = (1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24)
th = (1, 4, 9, 16)
n3600 = data[0] / np.array(data[0::4])
n7200 = data[1] / np.array(data[1::4])
n14400 = data[2] / np.array(data[2::4])
n28800 = data[3] / np.array(data[3::4])

plt.xlabel('thread')
plt.ylabel('accelerate factor')

plt.plot(th, n3600, label='n=3600', color='red',  marker='x')
plt.plot(th, n7200, label='n=7200', color='blue',  marker='x')
plt.plot(th, n14400, label='n=14400', color='green',  marker='x')
plt.plot(th, n28800, label='n=28800', color='yellow',  marker='x')
plt.plot(th, th, label='y=x', color='purple',  marker='x')

for a, b in zip(th, n3600):
    plt.text(a, b, '%.3f' % b, ha='center', va='bottom')
for a, b in zip(th, n7200):
    plt.text(a, b, '%.3f' % b, ha='center', va='bottom')
for a, b in zip(th, n14400):
    plt.text(a, b, '%.3f' % b, ha='center', va='bottom')
for a, b in zip(th, n28800):
    plt.text(a, b, '%.3f' % b, ha='center', va='bottom')
for a, b in zip(th, th):
    plt.text(a, b, '%.3f' % b, ha='center', va='bottom')

plt.legend()
plt.show()
