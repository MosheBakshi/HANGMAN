def is_valid_input(the_guess):
    """
    :param: the_guess:
    :type: string
    :return: if valid guess for the game
    :rtype: bool
    """

    ENGLISH_FLAG = the_guess.isascii()
    LENGTH_FLAG = len(the_guess) < 2
    SIGNS_FLAG = the_guess.isalpha()

    if (LENGTH_FLAG is False and  # IN CASE MORE THAN 1 LETTER BUT ELSE IS FINE
            ENGLISH_FLAG is True and
            SIGNS_FLAG is True):
        return False
    elif (LENGTH_FLAG is True and  # NOT IN ENGLISH AND SIGNS BUT IN LENGTH
          SIGNS_FLAG is False):
        return False
    elif (ENGLISH_FLAG is False or  # SAME AS UP BUT LONG STRING
          (SIGNS_FLAG is False and
           LENGTH_FLAG is False)):
        return False
    else:
        return True


def main():
    print(is_valid_input.__doc__)
    print(is_valid_input('a'))
    print(is_valid_input('A'))
    print(is_valid_input('$'))
    print(is_valid_input("ab"))
    print(is_valid_input("app$"))


if __name__ == '__main__':
    main()
