def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    :param: letter_guessed: old_letters_guessed:
    :type: string: list
    :return: if valid guess or already exists in the game
    :rtype: bool
    """

    ENGLISH_FLAG = letter_guessed.isascii()
    LENGTH_FLAG = len(letter_guessed) < 2
    SIGNS_FLAG = letter_guessed.isalpha()

    if (LENGTH_FLAG is False and  # IN CASE MORE THAN 1 LETTER BUT ELSE IS FINE
            ENGLISH_FLAG is True and
            SIGNS_FLAG is True):
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    elif (LENGTH_FLAG is True and  # NOT IN ENGLISH AND SIGNS BUT IN LENGTH
          SIGNS_FLAG is False):
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    elif (ENGLISH_FLAG is False or  # SAME AS UP BUT LONG STRING
          (SIGNS_FLAG is False and
           LENGTH_FLAG is False)):
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        old_letters_guessed.sort()
        return True


def main():
    print(try_update_letter_guessed.__doc__)
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters))
    print(try_update_letter_guessed('s', old_letters))
    print(old_letters)
    print(try_update_letter_guessed('$', old_letters))
    print(try_update_letter_guessed('d', old_letters))
    print(old_letters)


if __name__ == '__main__':
    main()
