# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 00:06:56 2019

@author: Asus
"""

def main():    
    number = int(input()) #we dont use this at all :D
    flower = [int(i) for i in input().split()]
    number_eliminated = 0
    i = 0
    #if(number < 3):
    #    print(1)
    #else:
    #    print(-1)
    if number == 2:
        if flower[0] == flower[1]:
            print(1)
        else:
            print(0)
    else:    
        while(i < number - 2):
            if(flower[i] > flower[i + 1] and flower[i + 1] < flower[i + 2]):
                i += 1
                continue
            if(flower[i] < flower[i + 1] and flower[i + 1] > flower[i + 2]):
                i += 1
                continue
            number_eliminated += 1
            flower.pop(i + 1)
            number -= 1
        print(number_eliminated)

if __name__ == '__main__':
    main()
