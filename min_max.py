

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return
   
    min_n = float('inf')
    max_n = float('-inf')

    for i in ints:
        if i < min_n:
            min_n = i
        if i > max_n:
            max_n = i
    
    return (min_n, max_n)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)

print ("Pass" if ((0, 999) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 0)]
random.shuffle(l)

print ("Pass" if (None == get_min_max(l)) else "Fail")

print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
