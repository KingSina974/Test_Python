#!/usr/bin/python3

#Part 0
print("\nSuccess\n")

#Part 1 Step 1.1 -Variables
fruit = "banana"
quantity = 3
pie_crust = "empty"
isOvenOn = False

print("You have", quantity, fruit,"and the pie crust is", pie_crust,"is the oven on ?", isOvenOn,'\n')

#Exercise 1.1.1
fruit = "apples"
quantity = 5
pie_crust = "empty"
isOvenOn = True

print("You have", quantity, fruit,"and the pie crust is", pie_crust,"is the oven on ?", isOvenOn,'\n')

#Step 1.2 -Functions
def print_hello_please():
    print("Hello\n")
print_hello_please()

def print_hello_with_my_name_please(myName):
    print("Hello", myName, '\n')
print_hello_with_my_name_please("Kovalen")

def calc_my_age_in_two_years(myCurrentAge):
    print("You are", myCurrentAge,"years old\n")
    my_age_in_two_years = myCurrentAge + 2
    return my_age_in_two_years
my_age_in_two_years = calc_my_age_in_two_years(33)
print("In two years, i'll be", my_age_in_two_years, "years old\n")

#Exercise 1.2.1
fruit = "apple"
quantity = 3
pie_crust = "empty"
isOvenOn = False

def prep_my_fruit(quantity, fruit, pie_crust):
    print("You put", quantity, fruit,"on the crust")
    pie_crust = "filled with delicious apples"
    return (pie_crust)

def turn_over_on(isOvenOn):
    isOvenOn = True
    return(isOvenOn)

pie_crust = prep_my_fruit(3, "apples", "empty")
print("my pie is", pie_crust)
print("Is the oven turned on ?", turn_over_on(isOvenOn),'\n')
