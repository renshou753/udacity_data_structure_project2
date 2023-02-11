PRECISION = 1e-3

def sqrt(number:int):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or type(number) != int:
        return None

    # calculate square root using binary search
    left = 0
    right = number
    
    while (right - left) > PRECISION:
        mid = (left + right) / 2
        if mid*mid > number:
            right = mid
        else:
            left = mid

    return int(round(left, 0))


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print ("Pass" if  (316228 == sqrt(100000000000)) else "Fail")
print ("Pass" if  (66666666667 == sqrt(4444444444444444444444)) else "Fail")
print ("Pass" if  (316228 == sqrt(100000000000)) else "Fail")
print ("Pass" if  (None == sqrt('')) else "Fail")
