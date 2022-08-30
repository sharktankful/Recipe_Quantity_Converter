recipe_name = input("Please enter in the name of your recipe here: ")

math_operator = input(
    f"Do you want {recipe_name} multiplied or divided? Enter here: ")

operator_lower = math_operator.lower()

while operator_lower != "multiplied" and operator_lower != "divided":
    print("\x1B[4m" + "This is not the correct choice." + "\x1B[0m")
    math_operator = input(
        f"Do you want {recipe_name} multiplied or divided? Enter here: ")
    operator_lower = math_operator.lower()

operator_amount = int(
    input(f"By how much do you want it {operator_lower}? Enter here: "))
