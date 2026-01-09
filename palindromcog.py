def is_palindrome(text):
    text = text.lower()
    reversed_text = text[::-1]
    if text == reversed_text:
        return "Palindrome"
    else:
        return "Not a Palindrome"
word = input("Enter a word: ")
print(is_palindrome(word))
