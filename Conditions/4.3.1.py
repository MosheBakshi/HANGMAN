user_input = input("Guess a letter: ")
ENGLISH_FLAG = user_input.isascii()
LENGTH_FLAG = len(user_input) < 2
SIGNS_FLAG = user_input.isalpha()

if (LENGTH_FLAG is False and  # IN CASE MORE THAN 1 LETTER BUT ELSE IS FINE
        ENGLISH_FLAG is True and
        SIGNS_FLAG is True):
    print("E1")
elif (LENGTH_FLAG is True and  # NOT IN ENGLISH AND SIGNS BUT IN LENGTH
      SIGNS_FLAG is False):
    print("E2")
elif (ENGLISH_FLAG is False or  # SAME AS UP BUT LONG STRING
      (SIGNS_FLAG is False and
       LENGTH_FLAG is False)):
    print("E3")
else:
    print(user_input)

"""
CHECKS THE USER'S INPUT IF LEGAL OR ILLEGAL -> IF LEGAL PRINTS THE INPUT ELSE PRINT THE RELEVANT ERROR
"""