#strings and Text.

#Line 4 is a variable whose value was formatted into line 5 .
types_of_people = 10
x = f"There are {types_of_people} types of people."

#Line 8 and 9 have variables whose string values was inserted  in line 10.
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x) #print the value of x.
print(y) #prints the value of y.

print(f"I said: {x}") #calls back and reprint the value of x.
print(f"I also said: '{y}'")

hilarious = False  #variablethat holda boolean value.
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious)) #another way of formatting text in a strings.

w = 'This is the left side of ...'
e = "a string with a right side."

print(w + e)
