



name = input("Please provide me with your name:\n")
while True:
    try:
        age = int(input("Please provide me with your age:\n"))
        if age <= 1:
            print("You cannot be that young")
            continue
        elif age >= 99:
            print("You cannot be that old")
            continue
        break
    except ValueError as error:
        print("Invalid age")
        print(f"Error message:\n{error}")
message = f"Hello {name}! in 10 years, you will be {age + 10} years old"
print(message)
with open("output.txt", "w") as file:
    file.write(message)
    print("Message written to output.txt file successfully")