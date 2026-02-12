"""PROGRAM FOR CHECKING THE GIVEN INPUT IS PALINDROME OR NOT
PROGRAM NAME: PALINDROME CHECKER
AUTHOR: AINEEN SAYYED
DATE CREATED: 6/02/2026"""


phrase = input("Enter a phrase/word/sequence:").strip().lower()
print(f"{'Yes It is Palindrome.'if phrase == phrase[::-1] else 'Not a Palindrome.'}")