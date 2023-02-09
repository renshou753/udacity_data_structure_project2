#### Code Design

Here because math library is not allowed to use, I am using binary search to gradually limit the scope of the range and eventually be able to find the approximate number closest to the square root.

#### Efficiency

This program does not take much of the space, it only needs three floating point variables to keep track of the left, mid and right value. So O(1) would be storage efficiency.

Time efficiency would be O(log n) for binary search algorithms.
