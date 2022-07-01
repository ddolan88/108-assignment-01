# <-- makes a comment

# variables are declared as such:
name = 'Derek'
last_name = 'Dolan'
age = 33
price = 12.33
found = False
valid = True
# first comes the variable then the value

# print is used like console.log
print("Hi" + name)

# print("hi, I am " + age + "years old ") will not work because python doesnt concatenate a string and numbers
# instead say print("Hi, I am ", age, "years old")

# if statements
if age < 100:
    print("No worries, its almost over!")

elif age == 100:
    print("whoah")

else:
    print("beyond old")

# functions


def hello():
    print("Line 1")
    print("Line 2")
    print("Line 3")


def say_hello():
    print("hello there")


print("Line 4")
# everything after the declared function that is on an indented line will be part of the function

hello()  # calls the function
say_hello()  # calls the function
say_hello()  # calls the function
say_hello()  # calls the function
say_hello()  # calls the function
