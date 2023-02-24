#variables are changed without my_infront
name = 'Rithubeth G'
age = 24
height = 73.6 #inches
weight = 231.5 #lbs
height_cm = round(height*2.54)

#Equation to find height in centimeters is defined here
weight_kg = round(weight*0.45)
#Equation to find weight in kilograms is defined here
eyes = 'Black'
teeth = 'White'
hair = 'Black'

#format strings are used as there are variables to be included

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, which is {height_cm} in centimeters.")
print(f"He's {weight} pounds heavy, which is {weight_kg} in kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the brushing.")

total = round(age + height_cm + weight_kg)
average = total/3
print(f"If I add {age}, {height_cm}, {weight_kg}, I get a total of {total} and an average of {average}.")

#round() command is used to round the respective values.

