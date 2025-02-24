from PIL import Image, ImageDraw, ImageFont


#1 + 2
try:
    a = 1/0
    print("This will not be printed")
except ZeroDivisionError as e:
    print("Cannot divide by zero", f"\n{e}")

#3
try :
    x = 1
finally :
    print("finally")
# Yes the code here is okay, it does the try command and the finally command

#4
# 'Except:' can catch any exception that the program runs into

#5
# it is wrong using the above way of catching exception because it will catch all exceptions possible
# and there are situations where you would rather your program to crash on an exception

#6
# the "except IOError" exception most commonly catches file related exceptions -
# - file does not exist
# - user has no permission to access the file
# - file already in use

# the "except ZeroDivisionError" exception catches when the program is trying to divide any -
# number by zero, which is impossible

#7 + 8 + 9
with open("./words.txt", "w") as file_write:
    file_write.write("Sergy")

with open("./words.txt", "r") as file_read:
    content = file_read.read()
    print(content)

#10
with open("./hebrew_words.txt", "w", encoding="UTF-8") as hebrew_file_write:
    hebrew_file_write.write("סרגיי ארטמונוב")

with open("./hebrew_words.txt", "r", encoding="UTF-8") as hebrew_file_read:
    hebrew_content = hebrew_file_read.read()
    print(hebrew_content)

#11
im = Image.new(mode = "RGB", size = (300, 300), color = (153, 153, 255))

text_param = {
    "text" : "Sergy Art",
    "font" : ImageFont.truetype("arial.ttf", size = 16),
    "text_color" : (255, 255, 255),
    "text_position" : (120, 150),
}

draw = ImageDraw.Draw(im)
draw.text(text_param["text_position"],
          text_param["text"],
          fill=text_param["text_color"],
          font=text_param["font"])
im.show()