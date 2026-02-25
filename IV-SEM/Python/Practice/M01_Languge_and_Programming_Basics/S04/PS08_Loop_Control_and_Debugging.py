# Loop Control and Debugging

"""
Debugging in Python :
    -->Bug is an error 
    -->Debugging is the process of finding and fixing bugs
Types of errors:
    1.Syntax Error  : Missing of colon, parenthesis, indentation etc
    2.Logical Error : Code runs but gives incorrect result(Missing of logic)
    3.Runtime Error : Any number divisible by "0"  raises runtime error
Debugging Techniques:
    1.Print() Statement Debugging         : Run the code line by line. and print variable values at different stages
    2.Using an IDE Debugger (try except)  : Most IDEs have built-in debuggers that allow you to set breakpoints, step through code, and inspect variables. 
    3.Python Debugger (using pdb module)  : -->To pause the Execution.
                                            -->To runn the code line by line.
                                            -->To inspect the values of variables at different stages of execution.
    -->Pdb Commands:
        1.n (next)      : Execute the next line of code.
        2.c (continue)  : Continue execution until the next breakpoint.
        3.q (quit)      : Exit the debugger and terminate the program.
        4.p (print)     : Print the value of a variable.
        5.l (list)      : Display the current location in the code.
        6.s (step)      : Step into a function call.
        7.r (return)    : Continue execution until the current function returns.
        8.h (help)      : Display a list of available commands.
"""

# Example of Print() Statement Debugging
"""
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = a+b
print("value of a is:", a)
print("value of b is:", b)
print("The sum is:", c)
"""

# Example of Using try-except for Debugging Run-time Errors
"""
try:
    a = int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError :
    print("Can not divide by zero")
except ValueError :
    print("Invalid input! Please enter a valid integer.")
"""

# Example of Using pdb module for Debugging
"""
import pdb
def add_numbers(x,y):
    pdb.set_trace()  # Set a breakpoint here
    return x + y
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("The sum is:", add_numbers(x,y))
"""
 