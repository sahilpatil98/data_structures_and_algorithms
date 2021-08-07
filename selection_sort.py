# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:21:24 2021

@author: Sahil Patil
"""
import random
randomlist = []
for i in range(0,5):
    n = random.randint(1,30)
    randomlist.append(n)



def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index
        

selection_sort(randomlist)