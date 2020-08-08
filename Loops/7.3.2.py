def check_win(secret_word, old_letters_guessed):
    """
    :param secret_word:
    :param old_letters_guessed:
    :return: returns True if player guessed all the letters of the hidden word
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def main():
    print(check_win.__doc__)
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))


if __name__ == '__main__':
    main()