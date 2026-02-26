
phrase = input("Enter a phrase/word/sequence:").strip().lower()
print(f"{'Yes It is Palindrome.'if phrase == phrase[::-1] else 'Not a Palindrome.'}")
