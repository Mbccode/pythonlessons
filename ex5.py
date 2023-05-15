#Formatting of String

name = 'Benjamin C. Mkpume'
age = 30
height = 69 #inches
weight = 154.30 #lbs
eyes = "blue"
teeth = "white"
hair = "black"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the food.")

# this line is tricky, try to get it exactly
total = age + height + weight
print(f"If I add {age},{height}, {weight} I get {total}")

#Writing variables that convert inches and pounds to centimeters and kilograms
print('_' * 20,) # This code will print underscore line 20 times

inch_1 = 2.54 #2.54cm
cm_1 = 0.394 #0.394 inch
convert_to_cm = height * inch_1
print("The result in centimeters:")
print(convert_to_cm, 'cm')

print('*' * 20) # This code will print hashtag 20 times

lbs_1 = 0.453 #0.454kg
kg_1 = 2.2 #2.2 pounds
convert_to_kg = weight * lbs_1
print("The result in kilograms:")
print(convert_to_kg, 'kg')

print('_' * 20) # This code will print underscore line 20 times
