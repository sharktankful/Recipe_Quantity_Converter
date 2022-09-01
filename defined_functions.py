# Checks if integer given is actually a integer
def prompt_for_int(prompt_str=None, error_str="\x1B[4m" + "Please enter in a number" + "\x1B[0m"):
    while True:
        try:
            return int(input(prompt_str))
        except ValueError:
            print(error_str, flush=True)
