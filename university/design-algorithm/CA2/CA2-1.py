# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:26:52 2019

@author: Asus
"""

def main():
    # getting the inputs
   n, m, k = [int(i) for i in input().split()]
   table = []
   empty_table = []
   for i in range(n):
       empty = []
       for j in range(m):
           empty.append([])
       empty_table.append(empty)
       
   for i in range(n):
       table.append([int(i) for i in input().split()])
       
if __name__ == '__main__':
    main()
