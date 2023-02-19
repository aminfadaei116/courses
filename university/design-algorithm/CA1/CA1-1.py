# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 00:06:14 2019

@author: Asus
"""
def checksum(arr):
    result = 1
    for i in range(len(arr)):
        result = (31 * result + arr[i]) % 1000003
    return result


def merge_unsort(arr, debug_numbers):
    n = len(arr)
    if n <= 1:
        return arr
    mid = int(n/2)  
    first = merge_unsort(arr[0 : mid], debug_numbers)
    second = merge_unsort(arr[mid : n], debug_numbers)
    return merge(first, second, debug_numbers)



def merge(first, second, debug_numbers):
    result = []
    while len(first) > 0 and len(second) > 0:
        temp = debug_numbers.pop()
        if temp == 1:
            result.append(first.pop(0))
        if temp == 2:
            result.append(second.pop(0))
            
    for i in first:
        result.append(i)
    for i in second:
        result.append(i)
    return result
    
def clean(arr):
    result = []
    for i in range(len(arr)):
        result.append(0)
    for i in range(len(arr)):
        result[arr[i] - 1] = i + 1
    return result

number = int(input())
aranged = [i for i in range(1, number + 1)]
debug_numbers = [int(i) for i in input()]
debug_numbers.reverse()
unclean = merge_unsort(aranged, debug_numbers)
clean = clean(unclean)
print(checksum(clean))





