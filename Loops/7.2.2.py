def numbers_letters_count(my_str):
    """
    :param my_str:
    :return: Counter list of digits and alphabetic characters in the string
    """
    counter_list = [0, 0]
    for char in my_str:
        if str(char).isdigit():
            counter_list[0] += 1
        else:
            counter_list[1] += 1
    return counter_list


def main():
    print(numbers_letters_count.__doc__)
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == '__main__':
    main()