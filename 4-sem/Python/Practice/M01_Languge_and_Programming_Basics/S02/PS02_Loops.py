# Loops 

"""
Loops are used to execute a block of code repeatedly until a certain condition is met.
Types of Loops in Python:
    1.For Loop:
        -->Used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
        -->Executes a block of code for each item in the sequence.
    2.While Loop:
        -->Repeats a block of code as long as a specified condition is true.
        -->The condition is checked before executing the loop body.
"""

# Example of For Loop
"""
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
while start <= end:
    if start % 2 == 0:
        print(start)
    start += 1
"""

# Example of While Loop 
"""
start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))
while start <= end:
    if start % 3 == 0 and start % 5 == 0:
        print("FizzBuzz")
    elif start % 3 == 0:
        print("Fizz")
    elif start % 5 == 0:
        print("Buzz")
    else : 
        print(start)
    start += 1
"""

# Print "Hello World" 5 times using for loop
"""
for i in range(0,5,1):
    print("Hello World")
"""

# Print N natural numbers and N natural numbers in reverse order
"""
n = int(input())
#  N natural numbers
for i in range(1,n+1):
    print(i,end=" ")
print()
#  N natural numbers in reverse order
for i in range(n,0,-1):
    print(i,end=" ")    
"""
# Print elements of a list using for loop
"""
li = [1,5,4,3,6,9,10]
for i in range(0,len(li),1):
    print(li[i],end=" ")
"""