# Practice Set 3: Operators

# Arithmetic Operators
"""
print("Arithmetic Operators:")
a = 15            
b = 4      
print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponentiation
"""

# Logical Operators
"""
# Logical Operators
print("Logical Operators:")
x = True
y = False
print("x and y:", x and y)   # Logical AND
print("x or y:", x or y)     # Logical OR
print("not x:", not x)       # Logical NOT
""" 

# Relational Operators
"""
print("Relational Operators:")
x = 10
y = 20
print("x > y:", x > y)      # Greater than
print("x < y:", x < y)      # Less than
print("x >= y:", x >= y)    # Greater than or equal to
print("x <= y:", x <= y)    # Less than or equal to
print("x == y:", x == y)    # Equal to
print("x != y:", x != y)    # Not equal to
"""

# Assignment Operators
"""
print("Assignment Operators:")
a = 5
print("Initial a:", a)
a += 3     # a = a + 3
print("After a += 3:", a)
a -= 2     # a = a - 2  
print("After a -= 2:", a)
a *= 4     # a = a * 4
print("After a *= 4:", a)
a /= 3     # a = a / 3
print("After a /= 3:", a)
a %= 5     # a = a % 5
print("After a %= 5:", a)
a **= 2    # a = a ** 2
print("After a **= 2:", a)
a //= 2    # a = a // 2
print("After a //= 2:", a)
"""

# Bitwise Operators
"""
print("Bitwise Operators:")
a = 60        # 60 = 0011 1100  
b = 13        # 13 = 0000 1101
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 2 =", a << 2) # Left Shift
print("a >> 2 =", a >> 2) # Right Shift
"""

# Memmbership Operators
"""
print("Membership Operators:")
s = "Hello, welcome to Python programming."
print("'welcome' in s:", 'welcome' in s)        # True  
print("'Python' not in s:", 'Python' not in s)  # False
"""

# Identity Operators
"""
print("Identity Operators:")
x = 10
y = 20
z = x
print("x is z:", x is z)          # True because both refer to same object
print("x is not y:", x is not y)  # True because values are different
x1 = [1,2,3]
y1 = [1,2,3]   
print("x1 is y1:", x1 is y1)          # False because values are different cause in memory they are stored at different locations
print("x1 is not y1:", x1 is not y1)  # True because values are different cause in memory they are stored at different locations
                          #MEMORY 
              #STACK                     #HEEP
                x            =            10
                y            =            20
                z            =            x
                x1           =            [1,2,3]
                y1           =            [1,2,3]
"""