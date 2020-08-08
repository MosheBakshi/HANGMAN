user_input = input("Please enter a string:").lower()
user_input = user_input[:len(user_input) // 2].lower() + \
             user_input[(len(user_input) - len(user_input) // 2) - 1:].upper()
print(user_input)
"""
make the string till the half be with lower letters and upper after the half size of the string
"""