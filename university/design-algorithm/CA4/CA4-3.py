# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:50:33 2020

@author: Asus
"""

def idk(acidi_list, iterator, n, sumi, fuck): 
    if n == iterator + 1:
        fuck.append(sumi + acidi_list[iterator])     
        return 
    in_chiz = iterator + 1
    idk(acidi_list, in_chiz, n, sumi, fuck)
    fuck.append(sumi + acidi_list[iterator])
    idk(acidi_list, in_chiz, n, sumi + acidi_list[iterator], fuck)
    
def main():
    n = int(input())
    acidi = []

    for i in range(n):
        info = input().split()
        if info[0] == "acid":
            acidi.append(int(info[1]) * int(info[2]))
        else:
            acidi.append(-int(info[1]) * int(info[2]))

    fuck = []
    sumi = 0
    iterator = 0

    idk(acidi, iterator, n, sumi, fuck)

    if 0 in fuck:
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
    