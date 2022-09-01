# Takes in the initial Recipe Name
recipe_name = input("Please enter in the name of your recipe here: ")


# Takes in whether were multiplying or dividing the ingredient amounts and puts
# the name in lowercase words
math_operator = input(
    f"Do you want {recipe_name} multiplied or divided? Enter here: ")
operator_lower = math_operator.lower()


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


# Asks for the first ingredient, amount, and measurement and puts it in one of the lists
ingredient = input("Enter in your first ingredient here:  ")
ingredient_lower = ingredient.lower()
ingredient_list.append(ingredient_lower)
while True:
    try:
        amount = int(input(f"Enter in the amount for {ingredient}: "))
    except ValueError:
        print("This is not a number")
        continue
    else:
        break
amount_list.append(amount)
measurement = input("What is the measurement?: ")
measurement_list.append(measurement)


# Keeps for asking for ingredients and measurements, stores them in the appropriate list
# and will keep asking until the word 'done' is typed in.
while ingredient != "done":
    ingredient = input(
        "Please enter in another ingredient or type 'Done' to finish: ")
    ingredient_lower = ingredient.lower()
    if ingredient == "done":
        break
    ingredient_list.append(ingredient_lower)
    amount = int(input(f"Enter in the amount for {ingredient}: "))
    amount_list.append(amount)
    measurement = input("What is the measurement?: ")
    measurement_list.append(measurement)


# Asks by what number do you want the ingredients multiplied or divided
operator_amount = int(
    input(f"By how much do you want it {operator_lower}? Enter here: "))
