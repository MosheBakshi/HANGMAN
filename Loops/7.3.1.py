def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word:
    :param old_letters_guessed:
    :return: String of the hidden word except the letters already guessed
    """
    new_string = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            new_string = new_string + letter
        else:
            new_string = new_string + ' _ '
    return new_string


def main():
    print(show_hidden_word.__doc__)
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))


if __name__ == '__main__':
    main()