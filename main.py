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
