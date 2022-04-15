# Check if Palindrome
# Checks if the string entered by the user is a palindrome. 
# That is that it reads the same forwards as backwards like “racecar”

text = input('Enter text for chek if palindrome: ')
new_text = text[::-1]
if text == new_text:
    print("It's a palindrome")
else:
    print("It's not a palindrome")