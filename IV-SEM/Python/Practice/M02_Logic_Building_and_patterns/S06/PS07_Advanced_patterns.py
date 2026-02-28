# Pascal's Triangle
 """
 -->Sample Input : 5
    Sample Output :     1
                        1 1
                        1 2 1
                        1 3 3 1
                        1 4 6 4 1

   n = int(input("Enter the number of rows: "))
   for i in range(n):
       num = 1
       for j in range(i + 1):
           print(num, end=" ")
           num = num * (i - j) // (j + 1)
       print()                   
 """

# Butterfly Pattern
 """
 -->Sample Input : 5
    Sample Output :     *       *
                        **     **
                        ***   ***
                        **** ****
                        *********
                        **** ****
                        ***   ***
                        **     **
                        *       *
 
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
"""