def count_chars(my_str):
    """
    :param my_str:
    :return: Dictionary of letters as a key and their counts as values
    """
    guessed_letters = []
    new_dict = {}
    for letter in my_str:
        if letter not in guessed_letters and letter != ' ':
            new_dict[letter] = my_str.count(letter)
    return new_dict


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))


if __name__ == '__main__':
    main()