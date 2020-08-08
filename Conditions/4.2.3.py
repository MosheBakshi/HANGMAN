user_input = str(input("Insert the temperature you would like to convert: "))
if user_input[-1].lower() == 'f':
    converted = str((5 * float(user_input[:len(user_input)-1]) - 160) / 9) + 'C'
elif user_input[-1].lower() == 'c':
    converted = str((9 * float(user_input[:len(user_input)-1]) + (32 * 5)) / 5) + 'F'
print(converted)

"""
PRINTING USER'S INPUT AS CONVERTED TEMPERATURE FROM C TO F OR F TO C OTHERWISE
"""