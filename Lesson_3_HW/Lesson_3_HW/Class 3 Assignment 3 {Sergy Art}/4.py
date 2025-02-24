


try:
    with open("data.txt", "rb") as file_binary_read:
        content = file_binary_read.read()
        with open("copy.bin", "wb")as file_binary_write:
            file_binary_write.write(content)
except FileNotFoundError as e:
    print("That file does not exist")
    print(f"Error message:\n{e}")