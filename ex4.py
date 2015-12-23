#Cars available for being driven
cars = 100
#Space available in a car
space_in_a_car = 4.0
#Amount of drivers
drivers = 30
#Amount of passengers to carpool
passengers = 90

#To calculate the amount of cars not driven, substract cars by drivers
cars_not_driven  = cars - drivers
cars_driven = drivers
#How many people fit in the cars
carpool_capacity = cars_driven * space_in_a_car
#What is the average of people per car we need
average_passengers_per_car = passengers/cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

#Study Drills
# The error that he got was because he added an extra _ to the variable
# thus the variable did not exist

#1. Space in a car does not need to be a float because you cannot 
# have half a person (or decimals for that matter) of a person 




