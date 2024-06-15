import math  # optional and you can delete this line if not useful


# subroutines if any, go here


# fill in mergesort
def mergesort(mlist):
    # Base case: if mlist is None or empty, return directly
    if mlist is None:
        return None
    elif len(mlist) <= 1:
        return mlist
    
    # Split the list into two havles
    mid = len(mlist) // 2
    left_half = mlist[:mid]
    right_half = mlist[mid:]

    # Recursively sort each half
    left_sorted = mergesort(left_half)
    right_sorted = mergesort(right_half)

    # merge the sorted half
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    # Merge elements from left to right into result list
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])  # Append from left list
            left_idx += 1
        else:
            result.append(right[right_idx])  # Append from right list
            right_idx += 1
            
    # Append remaining elements from left or right
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    
    return result


# Test cases
print(mergesort(None))
print(mergesort([]))
print(mergesort([7, 4, 3, 1, 7]))
