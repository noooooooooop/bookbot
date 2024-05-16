import re

def count_letters(path):
    letter_counts = {}

    with open(path) as f:
        file_contents = f.read()

        filtered = re.sub(r"[^a-zA-Z]", "", file_contents)

        for char in filtered:
            if not char.lower() in letter_counts:
                letter_counts[char.lower()] = 0

            letter_counts[char.lower()] += 1

        print(letter_counts)

def count_chars(path):
    with open(path) as f:
        file_contents = f.read()
        print(len(file_contents))

def count_words(path):
    with open(path) as f:
        file_contents = f.read()
        print(len(file_contents.split()))

if __name__ == "__main__":
    count_words("books/frankenstein.txt")
    count_chars("books/frankenstein.txt")
    count_letters("books/frankenstein.txt")
