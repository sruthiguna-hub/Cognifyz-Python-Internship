# Palindrome Checker
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")