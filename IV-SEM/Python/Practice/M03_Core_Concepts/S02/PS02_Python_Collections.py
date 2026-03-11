#Collections in Python
"""
1) List : ordered, mutable, allows duplicate elements
"""

# Creating a List
"""
a = [10, 20, 30, 40, 50]
print(a) 
b = list((10, 20, 312))
print(b)
"""

# Accessing List Elements
"""
a = [10, 20, 30, 40, 50]
print(a[0]) 
print(a[-1]) 
"""

# Creating list with repeated elements
"""
a = [10, 20, 30, 40, 50]
print(a*2) 
"""

# Adding elements to a List
"""
a = [10, 20, 30, 40, 50]
a.append(60)
print(a)
a.insert(2, 25)
print(a)
"""

# Removing elements from a List
"""
a = [10, 20, 30, 40, 50]
a.remove(30)
print(a)
a.pop(2)
print(a)
"""

# Slicing a List
"""
a = [10, 20, 30, 40, 50]
print(a[0:])
print(a[2:])
"""

# Reversing a List using slicing
"""
a = [10, 20, 30, 40, 50]
print(a[::-1])
"""

# leet code : 169. Majority Element
"""
def majorityElement(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for key, value in count.items():
        if value > len(nums) // 2:
            return key
nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
"""

# leet code : 88. Merge Sorted Array 
"""
def merge(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
"""
# leet code : 217. Contains Duplicate
"""
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))
"""

# Creation of set
"""
a = {10, 20, 30, 40, 50}
print(a)
b = set((10, 20, 30, 40, 50))
print(b)
"""
