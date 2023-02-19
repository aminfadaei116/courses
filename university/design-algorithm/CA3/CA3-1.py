# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:44:31 2019

@author: Asus
"""

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def main():
    n = int(input())
    cost = []
    complete = []
    ended = zerolistmaker(n + 1)
    result = 0
    for i in range(n):
        que = list(map(int, input().split()))
        cost.append(que)
        complete.append(zerolistmaker(n + 1))
        complete[i][i] = 1
    meet = list(map(int, input().split()))
    complete.append(zerolistmaker(n + 1))
    complete[n][n] = 1
    for i in range(n):
        cost[i].append(meet[i])
    cost.append(meet)
    cost[n].append(0)

    ended = 1
    selected = [0]
    maxi = max(max(cost))
    idk = [-1]
    for i in range(n):
        idk.append(maxi)
    i = 0
    while(ended != n + 1):
        temp = maxi
        i_best = -1
        j_best = -1
        for j in range(n + 1):

            if(idk[j] != -1 and idk[j] > cost[i][j]):
                idk[j] = cost[i][j]
            
            if(idk[j] != -1 and temp > idk[j]):
                temp = idk[j]
                i_best = i
                j_best = j
                
        i = j_best
        idk[j_best] = -1
        
        
        ended += 1
        result += temp
        
    print(result)
                
if __name__ == '__main__':
    main()
    

        
