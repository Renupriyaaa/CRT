# Loop Control

"""
Loop Control Statements in Python:
    -->Loop control statements change execution from its normal sequence.
    Types of Loop Control Statements:
        1.Break Statement:
            -->Used to terminate the loop prematurely when a certain condition is met.
            -->Control is transferred to the statement immediately following the loop.
        2.Continue Statement:
            -->Used to skip the current iteration of the loop and move to the next iteration.
            -->The remaining code inside the loop for the current iteration is skipped.
        3.Pass Statement:
            -->A null operation; it does nothing when executed.
            -->Used as a placeholder in loops, functions, or classes where code is syntactically required but no action is needed.
"""

# Example of Break Statement
"""
for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the loop body when i is 5
    print(i)
else:
    print("Loop completed normally without break.")
    if i == 8:
        print("This will not print because the loop was not broken.")
"""

"""
Password retry system(max 3 attemts)
if password is correct show"Login Successful"
else ask for password again3 times
and after 3 failed attemps show "Login Failed"
"""
# Password retry system
"""
p1 = "abc123"
for i in range(3):
    p2 = input("Enter your password: ")
    if p2 == p1:
        print("Login Successful")
        break
else:
    print("Login Failed")
"""