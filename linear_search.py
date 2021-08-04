# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:33:24 2021

@author: d0tamon
"""

def linear_search(list, target):
    """
    Returns index position of target if found, else None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 4)
verify(result)