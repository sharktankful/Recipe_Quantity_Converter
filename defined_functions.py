#Checks if integer given is actually a integer
def prompt_for_int(prompt_str=None, error_str="This is not an integer"):
    while True:
        try:
            return int(input(prompt_str))
        except ValueError:
            print(error_str, flush=True)