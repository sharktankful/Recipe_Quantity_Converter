from defined_functions import prompt_for_frac, prompt_for_int
from fractions import Fraction


# Takes in the initial Recipe Name
recipe_name = input("Please enter in the name of your recipe here: ")


# Takes in whether were multiplying or dividing the ingredient amounts and puts
# the name in lowercase words
math_operator = input(
    f"Do you want {recipe_name} multiplied or divided? Enter here: ")
operator_lower = math_operator.lower()

# If operator_lower equals multiplied or divided, this variable will equal these words
if operator_lower == "multiplied":
    size = "bigger"
elif operator_lower == "divided":
    size = "smaller"

# If the variable math_operator does not equal 'multiplied' or 'divided'
# the 'while loop' will keep asking for the correct word
while operator_lower != "multiplied" and operator_lower != "divided":
    print("\x1B[4m" + "This is not the correct choice." + "\x1B[0m")
    math_operator = input(
        f"Do you want {recipe_name} multiplied or divided? Enter here: ")
    operator_lower = math_operator.lower()


# Empty list to store the ingredients and the measurments for each ingredient
ingredient_list = []
amount_list = []
measurement_list = []
num_list = []
altered_list = []


# Asks for the first ingredient, amount, and measurement and puts it in one of the lists
ingredient = input("Enter in your first ingredient here: ")
ingredient_cap = ingredient.capitalize()
ingredient_list.append(ingredient_cap)
amount = prompt_for_frac(f"Enter in the amount for {ingredient}: ")
amount_list.append(amount)
measurement = input("What is the measurement?: ")
measurement_list.append(measurement.capitalize())


# Keeps for asking for ingredients and measurements, stores them in the appropriate list
# and will keep asking until the word 'Done' is typed in.
while ingredient != "Done":
    ingredient = input(
        "Please enter in another ingredient or type 'Done' to finish: ")
    ingredient_cap = ingredient.capitalize()
    if ingredient_cap == "Done":
        break
    ingredient_list.append(ingredient_cap)
    amount = prompt_for_frac(f"Enter in the amount for {ingredient}: ")
    amount_list.append(amount)
    measurement = input("What is the measurement?: ")
    measurement_list.append(measurement.capitalize())


# Generates the numberered order of ingredients entered in
count = 0
for x in ingredient_list:
    count += 1
    str_count = str(count)
    num_list.append(str_count + ".")


# Asks by what number do you want the ingredients multiplied or divided
operator_amount = prompt_for_int(
    f"By how much do you want your {recipe_name} recipe {operator_lower}? Enter here: ")


# Will take the data in amount_list and will either multiply or divide the data into a new list
for num in amount_list:
    if math_operator == "multiplied":
        mul = num * operator_amount
        frac_mul = str(Fraction(mul).limit_denominator())
        altered_list.append(frac_mul)
    elif math_operator == "divided":
        div = num / operator_amount
        frac_div = str(Fraction(div).limit_denominator())
        altered_list.append(frac_div)


# Takes the four lists with the collected data and prints them together to show the converted results
recipe_cap = recipe_name.upper()
print("----------------------------------------------------------------------------------")
print(f"This is your recipe {operator_lower} {operator_amount} times {size}:")
print('''
''')
print("\x1B[4m" + recipe_cap + " INGREDIENTS" + "\x1B[0m")
[print(w, x, y, z)
 for w, x, y, z in zip(num_list, altered_list, measurement_list, ingredient_list)]
print("----------------------------------------------------------------------------------")
