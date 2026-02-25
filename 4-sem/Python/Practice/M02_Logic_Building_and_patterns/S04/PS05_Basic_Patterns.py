# Square star parttenn
"""
-->Sample input : 4
   Sample output : * * * *
                   * * * *
                   * * * *
                   * * * *
                   
num = int(input())
for i in range(num):
   for j in range(num):
      print("*",end= " ")
   print()
"""

# Right Angle triangle
"""
-->Sample input : 4
   Sample output : * 
                   * * 
                   * * *
                   * * * *

num = int(input())
for i in range(1,num+1):
   for j in range(i):
      print("*",end=" ")
   print()
"""

#Inverted triangle
"""
-->Sample input : 4
   Sample output : * * * *
                   * * * 
                   * * 
                   * 

num = int(input())
for i in range(num):
   for j in range(num-i,0,-1):
      print("*",end =" ")
   print()
"""