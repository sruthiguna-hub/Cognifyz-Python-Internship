# File Manipulation - Word Counter
word_count = {}
with open("sample.txt", "r") as file:
    text = file.read().lower()
words = text.split()
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print("Word Count (Alphabetical Order):\n")

for word in sorted(word_count):
    print(f"{word} : {word_count[word]}")