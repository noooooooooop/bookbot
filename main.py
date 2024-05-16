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

        items = list((x, y) for (y, x) in letter_counts.items())
        items.sort(reverse=True)

        report = list(f"The '{letter}' character was found {count} times" for (count, letter) in items)

        return report

def count_chars(path):
    with open(path) as f:
        file_contents = f.read()

        return len(file_contents)

def count_words(path):
    with open(path) as f:
        file_contents = f.read()

        return len(file_contents.split())

if __name__ == "__main__":
    path = "books/frankenstein.txt"

    words = count_words(path)
    chars = count_chars(path)
    letter_counts = count_letters(path)

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")

    print("")

    for i in range(0, len(letter_counts)):
        print(letter_counts[i])
