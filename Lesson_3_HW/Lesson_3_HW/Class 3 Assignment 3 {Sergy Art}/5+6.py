from collections import defaultdict

#the story.txt story is taken from chatGPT

story_file_name = input("Please provide me with the story file name:\n")
word_count = defaultdict(int)
while True:
    try:
        with open(f"{story_file_name}.txt", "r", encoding="utf-8") as story_file:
            for line in story_file:
                words = line.lower().split()
                for word in words:
                    word = word.strip(".,!?()[]{}\"'’’“")
                    word_count[word] += 1

        with open("word_count.txt", "w", encoding="utf8") as word_count_file:
            for word, count in word_count.items():
                word_count_file.write(f"{word}: {count}\n")

        break
    except FileNotFoundError as e:
        print(f"File name not found\nError message: {e}")