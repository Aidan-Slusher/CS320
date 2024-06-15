# Determine if a list is made up of a repeating pattern

import math  # Optional and you can delete this line if not useful

# Subroutines if any, go here

# Fill in repeat


def repeat(list):
    if list is None:
        return None
    
    length = len(list)
    longest_pattern = None
    
    for pattern_length in range(1, length // 2 + 1):
        pattern = list[:pattern_length]
        repeated_pattern = True
        
        for i in range(pattern_length, length, pattern_length):
            if list[i:i + pattern_length] != pattern:
                repeated_pattern = False
                break
            
        if repeated_pattern and (longest_pattern is None or len(pattern) > len(longest_pattern)):
            longest_pattern = pattern
        
    return longest_pattern


# Test cases
print(repeat(['a', 'b', 1, 'b', 'a', 'b', 1, 'b']))
# Output: ['a', 'b', 1, 'b']

print(repeat(['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']))
# Output: ['a', 'b']

print(repeat(['a', 'b', 'a', 'b', 'a', 'b', 'c']))
# Output: None

print(repeat([1]))
# Output: None

print(repeat(None))
# Output: None
