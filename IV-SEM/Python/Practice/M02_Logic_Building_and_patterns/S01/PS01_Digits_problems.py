# Solution 1:  Using Mathematical Operations
"""
-->Sample input : 1234
   Sample output : 4

-->Sample input : 56789
   Sample output : 5

****----First Solution----****

num = int(input("Enter a number: "))
if num == 0:                # If the number is 0, it has 1 digit
    num_digits = 1          # If the number is negative, convert it to positive
else:                       
    num_digits = 0          # Initialize digit count
    while num > 0:          # Loop until the number becomes 0
        num = num // 10     # Remove the last digit from the number
        num_digits += 1     # Increment digit count for each division by 10
print("Number of digits:", num_digits)

****----Second Solution----****

num = int(input("Enter a number: "))
count = 0
while num > 0 :
    count += 1
    num = num // 10
print("Number of digits:", count)
"""

# Solution 2: Using String Conversion
"""
-->Sample input : 1234
   Sample output : 10

-->Sample input : 12236
   Sample output : 14

num = int(input("Enter a number: "))
count = 0
while num > 0:
    digit = num % 10  # s +=(num % 10)
    count += digit    # **--Ignore--**
    num = num // 10   # num = num // 10
print("Sum of digits:", count)  #print(s)
"""

# Solution 3: print even digits in the number
"""
-->Sample input : 1234
   Sample output : 24

-->Sample input : 12236
   Sample output : 226

num = int(input("Enter a number: "))
even_digits = ""   # **--Ignore--**
while num > 0:
    digit = num % 10
    if digit % 2 == 0:  
        even_digits = str(digit) + even_digits  # print(digit, end=" ")
    num = num // 10
print("Even digits in the number:", even_digits)
"""

# Solution 4: Reverse the digits of the number
"""
-->Sample input : 1234
   Sample output : 4321

-->Sample input : 12236
   Sample output : 63221

****----First Solution----****

num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
      digit = num % 10
      reversed_num = reversed_num * 10 + digit
      num = num // 10
print("Reversed number:", reversed_num)

****----Second Solution----****

def reverse_number(num):
      reversed_num = 0
      while num > 0:
            digit = num % 10  # **--Ignore--**
            reversed_num = reversed_num * 10 + digit  # reversed_num = reversed_num * 10 + digit
            num = num // 10
      return reversed_num 
num = int(input("Enter a number: "))
while num > 0:
      digit = num % 10
      if digit % 2 == 0:    # **--Ignore--**
            print(digit, end=" ") # **--Ignore--**
      num = num // 10
#print("Reversed number:", reverse_number(num))
"""
   
