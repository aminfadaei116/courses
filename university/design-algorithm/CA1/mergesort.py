# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:25:16 2019

@author: Asus
"""

def checksum(arr):
    result = 1
    for i in range(len(arr)):
        result = (31 * result + arr[i]) % 1000003
    return result


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = int(n/2)
    
    first = merge_sort(arr[0: mid])
    second = merge_sort(arr[mid: n])
    return merge(first, second)

def merge(arr1, arr2):
    result = []
    while len(arr1) > 0 and len(arr2):
        if arr1[0] < arr2[0]:
            print(1)
            result.append(arr1[0])
            arr1.pop(0)
        else:
            print(2)
            result.append(arr2[0])
            arr2.pop(0)
    for i in arr1:
        result.append(i)
    for i in arr2:
        result.append(i)
    return result


input_list = [int(i) for i in input().split()]
res = merge_sort(input_list)
print(res)
print(checksum(input_list))
