# Variables and Names

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

#this linne of code prints cars that is available
print("There are", cars, "cars available.")
#here prints numbers of drivers
print("There are only", drivers, "drivers available.")
#numbers of cars driven
print("There will be", cars_not_driven, "empty cars today.")
#possible numbers of people that can be transported
print("We can transport", carpool_capacity, "people today.")
#numbers of people that can be transported
print("We have", passengers, "to carpool today.")
#passengers'average
print("We need to put about", average_passenger_per_car, "in each car.")
