# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:29:31 2021

@author: Sahil Patil
"""

def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of list and divide into sublist
    Conquer: Recursively sort the sublist created
    Combine: Merge the sorted sublist created in previous step
    Take O(kn log n) time
    """
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)
    
def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Take overall O(k log n) time
    """
    
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    
    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in process
    Returns new merged list
    Runs in overall O(n log n)
    """
    
    ls = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ls.append(left[i])
            i += 1
        else:
            ls.append(right[j])
            j += 1
            
            
    while i < len(left):
        ls.append(left[i])
        i += 1
        
    while j < len(right):
        ls.append(right[j])
        j += 1
        
    return ls


def verify_sorted(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54,12,45,32,63,1,20]

l = merge_sort(alist);
print(l)

print(verify_sorted(alist))
print(verify_sorted(l))