import os.path

if os.path.exists("data.txt"):
    print("File exists, opening in append mode")
else:
    print("File does not exist, creating it")

with open("data.txt", "a") as file_write:
    for i in range(1,6):
        file_write.write(f"line number: {i}\n")
    file_write.write("\n")

with open("data.txt", "r") as file_read:
    content = file_read.read()
    print(content)