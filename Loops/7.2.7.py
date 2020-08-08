def arrow(my_char, max_length):
    """
    :param my_char:
    :param max_length:
    :return:Creates string in shape of arrow, made of the char and the tip will be in length of the max_length
    """
    arrow_string = ""
    for i in range(1, max_length * 2):
        if i < max_length:
            arrow_string = arrow_string + (my_char * i + '\n')
        elif i >= max_length:
            arrow_string = arrow_string + (my_char * (max_length * 2 - i) + '\n')
    return arrow_string


def main():
    print(arrow.__doc__)
    print(arrow('*', 5))


if __name__ == '__main__':
    main()