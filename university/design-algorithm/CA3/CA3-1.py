# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 12:44:31 2019

@author: Asus
"""
#def show_list(vec):
#    for i in range(len(vec)):
#        print(vec[i])
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

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
## getting the inputs

#show_list(cost)
#show_list(complete)

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
    
    
#    for i in selected:
#        for j in range(n + 1):
#            
#            if(cost[i][j] < temp and complete[i][j] == 0 and (j not in selected)):
#
#                temp = cost[i][j]
#                i_best = i
#                j_best = j
#    selected.append(j_best)
#    complete[i_best][j_best] = 1
#    complete[j_best][i_best] = 1
    ended += 1
#    print("temp is")
#    print(temp)
#    print(i_best, j_best)
#    print("____")
    result += temp
    
print(result)
                

    

        
