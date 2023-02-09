from merge_sort import merge_sort

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    # first use merge sort to sort the array, merge sort has time complexity of O(n logn)
    merge_sort(input_list, 0, len(input_list)-1)
    input_list.reverse()

    lst1 = []
    lst2 = []

    for idx, v in enumerate(input_list):
        if idx % 2 == 0:
            lst1.append(str(v))
        else:
            lst2.append(str(v))

    result = [int(''.join(lst1)), int(''.join(lst2))]
    
    return result
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_function([[5, 6, 9, 8, 7], [975, 86]])

test_function([[1, 0, 1], [10, 1]])


