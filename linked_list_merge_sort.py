# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:55:40 2021

@author: Sahil Patil
"""

from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublist containing a single node
    - Repeatedly merge the sublist to produced sorted sublists until one remains
    
    Returns a sorted linked list
    
    Runs in O(kn log n) time
    """
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublist
    
    Takes O(k log n) time
    """
    
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        
        return left_half,right_half
    else:
        size = linked_list.size()
        mid = size//2
        
        mid_node = linked_list.node_at_index(mid-1)
        
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
    
def merge(left, right):
    """
    Merges two linked list, sorting by data in nodes
    Returns a new, merged list
    Runs in linear time
    """
    
    #Create new linked list that contains node from
    #merging left and right
    merged = LinkedList()
    
    
    #Add fake head discarded later
    merged.add(0)
    
    #Set current to the head of the linked list
    current = merged.head
    
    #Obtain head nodes for left and right linked list
    left_head = left.head
    right_head = right.head
    
    #Iterate over left and right until we reach tail node of either
    
    while left_head or right_head:
        #If head node of left is None, we're past the tail
        #Add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            #call next on right to set loop condition to False
            right_head = right_head.next_node
        #If head node of right is None, we're past the tail
        #Add the tail node from left to merged list
        elif right_head is None:
            current.next_node = left_head
            #Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            #Not at either tail node
            #Obtain node data to perform comparison
            left_data = left_head.data
            right_data = right_head.data
            #If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                #Move left head to next node
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                #Move right head to next node
                right_head = right_head.next_node
            #Move current to next node
            current = current.next_node
    
    #Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    
    return merged
    
#Test

ls = LinkedList()
ls.add(1)
ls.add(234)
ls.add(14)
ls.add(24)

print(ls)

sorted_linked_list = merge_sort(ls)
print(sorted_linked_list)