import random
import string

# The user must enter the password length
passwordlength = int(input("Enter the password length : "))

# Define the characters that will be used to generate the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for i in range(passwordlength))

# Show the password
print("The password is:", password)
