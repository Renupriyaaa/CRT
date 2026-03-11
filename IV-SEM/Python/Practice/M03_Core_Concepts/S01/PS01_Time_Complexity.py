# Time Complexity :
                # time required to run an algorithm  based upon the size of the input data 

"""
big O notation : used to represent the time complexity of an algorithm
O(1) : constant time complexity
O(n) : linear time complexity
O(n^2) : quadratic time complexity
O(n log n) : linearithmic time complexity
O(2^n) : exponential time complexity
O(log n) : logarithmic time complexity  

"""

# O(1) : constant time complexity
"""
def constant_time(arr):
    return arr[0]
print(constant_time([10,20,30]))
"""

# O(n) : linear time complexity
"""
def linear_time(arr):
    for i in arr:
        print(i)
print(linear_time([10,20,30]))
"""

# O(n^2) : quadratic time complexity
"""
def quadratic_time(arr):
    for i in arr:
        for j in arr:
            print(i, j)
print(quadratic_time([10,20,30]))
"""

# O(n log n) : linearithmic time complexity
"""
def linearithmic_time(arr):
    return sorted(arr)
print(linearithmic_time([10,20,30]))
"""

# O(2^n) : exponential time complexity
"""
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input())
print(fibo(n))
"""