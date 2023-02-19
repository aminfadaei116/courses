# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:14:48 2019

@author: Asus
"""


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def inflistmaker(n):
    listofzeros = [float("inf")] * n
    return listofzeros

info = list(map(int, input().split()))
n, s, t = info[0], info[1], info[2]
elev = []
for i in range(n):
    elev.append(list(map(int, input().split())))
    
    
test = float("inf")
maxi = max(max(elev))

connect = []

for i in range(maxi+1):
    connect.append(zerolistmaker(maxi+1))

for k in range(n):
    for i in range(1, len(elev[k])):
        for j in range(i+1, len(elev[k])):
            connect[elev[k][i]][elev[k][j]] = 1
            connect[elev[k][j]][elev[k][i]] = 1
wow = []        
for i in range(maxi):
    temp = []
    for j in range(maxi):
        if connect[i][j] == 1:
            temp.append(j)
    wow.append(temp)

dist = inflistmaker(maxi)
dist[s] = 0
hast = zerolistmaker(maxi)
hast[s] = 1
what = 1
fisrt = s
while(what != maxi):
    che = []
    for i in range(len(wow[s])):
        if dist[wow[s][i]] > abs(wow[s][i] - s) + dist[s]:
            dist[wow[s][i]] = abs(wow[s][i] - s) + dist[s]
            che.append(abs(wow[s][i] - s) + dist[s])
    kk = dist.index(min(dist))
    hast[kk] = 1
    s = kk
    what += 1
    
print(dist)

    
    
    
    


