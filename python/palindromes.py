# Enter text
text = input("Enter a phrase: ")

# We remove whitespace and convert text to lowercase for case-insensitive comparison
text = text.replace(" ", "").lower()

# Compare the original text with its reverse to determine if it is a palindrome
if text == text[::-1]:
	print("The text is a palindrome.")
else:
	print("The text is not a palindrome.")
