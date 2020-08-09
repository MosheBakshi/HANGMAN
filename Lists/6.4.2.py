def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    :param: the_guess:
    :type: string
    :return: if valid guess or already exists in the game
    :rtype: bool
    """

    ENGLISH_FLAG = letter_guessed.isascii()
    LENGTH_FLAG = len(letter_guessed) < 2
    SIGNS_FLAG = letter_guessed.isalpha()

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
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def main():
    pass


if __name__ == '__main__':
    main()
