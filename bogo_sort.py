# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:14:10 2021

@author: Sahil Patil
"""

import sys
import load

numbers = load.load_numbers(sys.argv[1])

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
        return True
    
def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values