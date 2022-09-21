import math
import random

string_value = "h"
print(string_value)

string_value = 'h'
# This is the empty string:
string_value = ""
print(string_value)

class_credits = 3
class_grade = 4.0
print(f"The number of credits for the class"
      f" is {class_credits}.")
print(class_grade)
# Try using formatted strings (f-strings).
print(f"The quality points are:\n\t{class_credits*class_grade}.")
# There are escape characters "\n" and "\t" for newline character and tab.
# You can call a method on a string (upper, lower, title, rstrip, and lstrip).
msg = "     hEllo wOrld"
print(msg)
# Calling a function like print doesn't take dot notation.
print()
# Call the lower method on msg using dot notation.
# Calling a method takes dot notation.
print(msg.lower())
# Here the returned value is "HELLO WORLD" is not printed.
msg.upper()
# Here the returned value is "HELLO WORLD" is printed.
print(msg.upper())

print(msg.title())
print(msg)

print(msg.lstrip())

# Import and use the libraries math and random.
# Look inside the math library to call the sqrt function!
print(math.sqrt(9))

# Look inside the random library to call the randrange function and
# generate one of two random numbers, 0 or 1.
print(random.randrange(2))
print(random.randrange(2))
print(random.randrange(2))
print(random.randrange(2))


