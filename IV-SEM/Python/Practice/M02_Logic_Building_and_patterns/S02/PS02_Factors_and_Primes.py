#Print all the factors of a given number 
"""
-->Sample input : 12
   Sample output : 1 2 3 4 6 12

****----First Solution----****

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

****----Second Solution----****

num = int(input("Enter a number: "))
for i in range(1,n//2 + 1):
    if n % i == 0:
        print(i, end=" ")
print(n)  
"""
# Count number of factors for a given number
"""
-->Sample input : 12
   Sample output : 6

***--First Solution----**

num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1
print("Number of factors:", count)

***--Second Solution----**

num = int(input("Enter a number: "))
count = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        count += 1
print("Number of factors:", count + 1)  # +1 for the number itself
"""
# Check whether a given number is prime or not
"""
-->Sample input : 7
   Sample output : prime number
-->Sample input : 9
   Sample output : not a prime number

****----First Solution----****

num = int(input("Enter a number: "))
if num < 2:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

***----Second Solution----**

num = int(input("Enter a number: "))
count = 0
for i in range(2,num//2 + 1):
    if num % i == 0:
        count += 1
if count == 0 and num > 1:
    print("Prime number")
else:
    print("Not a prime number")

# Ternary operator to check if a number is prime or not

num = int(input("Enter a number: "))
is_prime = "Prime number" if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)) else "Not a prime number"
print(is_prime)
"""

# Print all the prime factors in the given number
"""
-->Sample input : 1 10
   Sample output : 2 5 7

****----First Solution----**

num = int(input("Enter a number: "))
print("Prime factors of", num, "are:", end=" ")
for i in range(2, num + 1):
    while num % i == 0:
        print(i, end=" ")
        num //= i

****----Second Solution----**

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
for i in range(start, end + 1):
    count = 0"
    for j in range(2, i//2 + 1):
        if i % j == 0:
            count += 1  
if count == 0 and i > 1:
    print(i, end=" ")
"""

# Read a number from the user and display factorial of that number
"""
-->Sample input : 5
   Sample output : 120

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)
"""

# Read a number from the user and display the sum of all the factors of that number

class solution:
    def reverse(self , x: int) -> int:
        if x < 0:
            x = -1 * x
            rev = int(str(x)[::-1])
            return -1 * rev
        else:
            rev = int(str(x)[::-1])
            return rev