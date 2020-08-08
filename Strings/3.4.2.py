user_input = input('Please enter a string:').lower()
first_letter = user_input[0]
replaced_input = first_letter + user_input[1:].replace(first_letter, "e")
print(replaced_input)
"""
replace all the letters as the first letter except the 1st itself
"""