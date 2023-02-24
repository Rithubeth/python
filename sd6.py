types_of_people = 10
#a variable is defined
x = f"There are {types_of_people} types of people."
#x is a variable defined with a format string.And this format string contains a variable.
binary = "binary"
do_not = "don't"
#2 variables are defined with strings 
y = f"Those who know {binary} and those who {do_not}."
#same as x here y is defined with a format string containing 2 variables.
print(x)
print(y)
#command to print is given
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#2 variables. One contains a empty literal.
print(joke_evaluation.format(hilarious))
#command to print joke evaluation as False.empty literal is defined using .format command.
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
#variables w and e are added and displayed together.

#In this script in line 13,14 strings are put inside strings. In line 8 the format string contains two variables which are defined as strings in line 5 and 6.
#+ is an addition operation. When the string w is added with e, both strings are combined as one single string.
