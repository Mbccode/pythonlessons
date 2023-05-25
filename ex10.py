#Exercise 10
# Escaping quotes ("" and '') with backlash '\'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm splint\non line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
  \t* Cat food
  \t* Fishies
  \t* Catnip
  \r* Grass
  """ # Carriage return '\r'

age = "13 years old"
height = "5'8\""
discript_self = f"I'm {age} and {height} tall."
self = "And {} in complexion.".format('fair')
name = "My name is {}."
na_me = "Robert Philip"

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(discript_self, end = " ")
print(self)
print(name.format(na_me))
print(fat_cat)
