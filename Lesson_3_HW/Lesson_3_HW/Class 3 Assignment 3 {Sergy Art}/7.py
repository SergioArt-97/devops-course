

def user_num(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError as e:
            print(f"Invalid number\nError message:{e}")


first_number = user_num("Please provide me with the first number:\n")

while True:
    second_number = user_num("Please provide me with the second number:\n")
    try:
        result = first_number/second_number
        print(f"{first_number} / {second_number} = {result:.2f}")
        break
    except ZeroDivisionError as e:
        print(f"cannot divide by zero\nError message:{e}")