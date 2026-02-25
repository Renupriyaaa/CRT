# Practice Set 2: Variable and Data Type

"""
Data Types in Python:
          1.Fundamental Data Types:
                a. int : Integer type to represent whole numbers (without decimal point)
                b. float : Floating-point type to represent decimal numbers
                c. boolean : Boolean type to represent True or False 
                d. string : String type to represent text ('hello', "hello")
                e. complex : Complex type to represent complex numbers(a + bj==>a+bi) 
          2.Collection Data Types:
                a. list : Ordered, mutable collection of items
                b. tuple : Ordered, immutable collection of items
                c. set : Unordered collection of unique items
                d. dictionary : Unordered collection of key-value pairs
"""

# Fundamental Data Types Examples
"""
x = 10               # int
y = 12.45             # float
z = 5 + 6j          # complex
print(x,type(x))   
print(y,type(y))   
print(z,type(z))    
f1 = 12e2          # float
f2 = 5E3          # float
print(f1,type(f1))    
print(f2,type(f2))  
a = True           # boolean
b = False          # boolean
print(a,type(a))   
print(b,type(b))  
s1 = 'Hello'       # string
s2 = "World"       # string
print(s1,type(s1)) 
print(s2,type(s2)) 
"""

# Complex Number Operations
"""
c1 = 5+4j      # complex
c2 = complex(2,-3)  # complex
print(c1,c2)
# Arithmetic operations
print(c1 + c2)
print(c1 * c2)
print(c1 - c2)
print(c1 / c2)
# Accessing real and imaginary parts
print(c1.real, c1.imag)
print(c2.real, c2.imag)
"""

# Boolean Operations
"""
b1 = True    # value of boolean is 1
b2 = False   # value of boolean is 0
print(b1 + 5)    # 6
print(b2 + 5)    # 5  
"""

# String Operations
"""
s1 = "Hello"      # string    
s2 = 'World'      # string
s5 = '''line 1
        line 2
        line 3'''          # multi-line string
print(s1)
print(s2)
print(s5)
# Concatenation
s3 = s1 + " " + s2      
print(s3)
# Repetition      
s4 = s1 * 3
print(s4)
# Accessing characters
print(s1[0])      # H
print(s2[1])      # o
# Slicing   
print(s3[0:5])    # Hello
print(s3[6:])     # World
# Step slicing
print(s3[::2])    # Hello
# Length of string
print(len(s3))    # 11
# Changing case
print(s3.upper()) # HELLO WORLD
print(s3.lower()) # hello world
# Finding substring
print(s3.find("lo"))  # 3
print(s3.find("z"))   # -1 (not found)    
# Replacing substring
print(s3.replace("World", "Python"))  # Hello Python  
# Splitting string
words = s3.split(" ")   # ['Hello', 'World']    
print(words)
"""