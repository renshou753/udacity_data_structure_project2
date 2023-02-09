

def merge(array: list, left: int, mid: int, right: int) -> None:
    """
    Merges two sorted region of an array into an combined sorted region.

    Args:
        array (list): array of elements
        left (int): starting index of first region
        mid (int): mid index of first region
        right (int): last index of right region
    Returns:
        None
    """
    size = right - left + 1
    temp = [None for _ in range(size)]

    first = left  # left index
    second = mid + 1 # right index
    for i in range(size):
        if first > mid: # left side is already sorted, choose right index
            temp[i] = array[second]
            second += 1
        elif second > right: # right side sorted, choose left index
            temp[i] = array[first]
            first += 1
        elif array[first] > array[second]: # left > right, choose right
            temp[i] = array[second]
            second += 1
        else:
            temp[i] = array[first] # right > left, choose left
            first += 1

    # replace original array
    for i in range(size):
        array[left+i] = temp[i]


def merge_sort(array: list, left: int, right: int):
    """
    Driver function for merge sort.
    """
    if left >= right:
        return    # stop if length=1

    # devide
    mid = (left + right) // 2
    merge_sort(array, left, mid)
    merge_sort(array, mid+1, right)

    # merge
    merge(array, left, mid, right)
