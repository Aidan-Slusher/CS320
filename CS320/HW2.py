# extract values from a sorted list

import math  # optional and you can delete this line if not useful


# subroutines if any, go here

def binary_search(arr, target, is_left):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target or (is_left and arr[mid] == target):
            right = mid
        else:
            left = mid + 1
    return left


# your subroutine goes here
def extract(list, lo, hi):
    if list is None:
        return None
    
    if lo is None:
        start_index = 0
    else:
        start_index = binary_search(list, lo, True)
        
    if hi is None:
        end_index = len(list)
    else:
        end_index = binary_search(list, hi, False)
    
    if lo is not None and hi is not None and lo > hi:
        return None
    
    return list[start_index:end_index]
