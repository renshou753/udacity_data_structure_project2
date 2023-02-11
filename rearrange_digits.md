#### Code Design

Because the target is to find the two numbers such that their sum are maxiumum, first the array needs to be sorted, merge sort is used in this case. After the array is sorted the program loop through the sorted array to put the digit into either list1 or list2 depends on whether the digit can be divided by 2. The idea is that we need to put the biggest digit into its corresponding position for both lists so has to do it one by one in conjuction.

#### Efficiency

Time efficiency is O(n logn) for merge sort, afterwards a loop is used to put the digit into its position and it has O(n) for time complexity, on average the time efficiency is O(n logn).

For storage efficiency, in order to save the digits, two lists are used, O(n) storage for list and another O(logn) for merge sort function stack. 
