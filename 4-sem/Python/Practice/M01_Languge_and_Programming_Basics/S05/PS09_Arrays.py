# Arrays
"""
It is a collection of homogeneous data elements that can store under a single variable name python does not support arrays.

--> NumPy :
           1) Numpy-->Numerical python
           2)It can easily access arrays
           3)Maily uses in ML,DS,AI Applications
    The index values start wuth 0 and ends with (n-1), n-->Size of the array
"""

# NumPy Array Operations
"""
import numpy as np
arr = np.array([10, 20, 30])
print("Numpy array:", arr)
print(np.max(arr))  # Maximum value in the array
print(np.min(arr))  # Minimum value in the array
print(np.mean(arr)) # Mean of the array elements
print(np.median(arr)) # Median of the array elements
print(np.sum(arr))  # Sum of all elements in the array
print(np.zeros(8))  # Create an array of zeros with the same shape as arr
print(np.ones(5))  # Create an array of ones with the same shape as arr
print("Even numbers from list:", np.arange(2,10,2))  # Even numbers from 2 to 10
print("Odd numbers from list:", np.arange(1,10,2))   # Odd numbers from 1 to 10
"""
# User Input Array

import numpy as np
n = int(input("Enter the size of the array: "))
ele = list(map(int, input("Enter the elements: ").split()))
print("Array elements are:", np.array(ele))