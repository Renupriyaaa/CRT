# Intermediate Patterns
"""
-->Sample Input  : [1,2,3,4,5]
   Sample Output : [1,4,9,16,25]

***----First Solution----**    

li = [1,2,3,4,5]
for i in range(len(li)):
    li[i] = li[i] ** 2
print(li)

***----Second Solution----**
li = [1,2,3,4,5]          |
res=[]                    |
for i in li:              |  ans = [i ** 2 for i in li]
    res.append(i**2)      |  print(ans)
print(res)                |
"""

# extracting even numbers from a list
"""
-->Sample Input  : [1,2,3,4,5]
   Sample Output : [2,4]

li = [1,2,3,4,5]           |
res = []                   |      
for i in li:               |   ans = [i for i in li if i % 2 == 0]  
    if i % 2 == 0:         |   print(ans)
        res.append(i)      |    
print(res)                 |
"""

# converting list of characters to a string
"""
--->Sample Input  : ['a','b','c]
    Sample Output : 'a b c'

**----First Solution----**

li = ['a','b','c']           
res = ''
for i in li:
    res += i + ' '
print(res.strip())

**----Second Solution----**

li = ['a','b','c']
res = ""
for ch in li:
    res = res + ch + " "
print(res)
print("@".join(li))
"""

# printing a pattern
"""
-->Sample Input  : 4
   Sample Output :     *
                      * *
                     * * *
                    * * * *

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
"""

# Invertedpiramid pattern
"""
-->Sample Input  : 4
   Sample Output : * * * *
                    * * *
                     * *
                      *

n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
"""

# Diamond pattern
"""
-->Sample Input  : 4
   Sample Output :     *
                      * *
                     * * *
                    * * * *
                     * * *
                      * *
                       *                                        

n = int(input("Enter the number of rows: "))
# Upper half of the diamond
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
# Lower half of the diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
"""

# Number pattern
"""
--> Sample Input  : 4
    Sample Output :     1
                       1 2
                      1 2 3
                     1 2 3 4

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))    
"""

# Hollow Pyramid pattern
"""
--> Sample Input  : 4
    Sample Output :     *
                       * * 
                      *   *
                     * * * *

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print("* " * n)
    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
"""