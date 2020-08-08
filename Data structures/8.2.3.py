def mult_tuple(tuple1, tuple2):
    """
    :param tuple1:
    :param tuple2:
    :return: cartesian product of tuples
    """
    a = []
    for c in tuple1:
        for b in tuple2:
            a.append((c, b))
            a.append((b, c))
    return a


def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple), '\n', '\n')
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(mult_tuple(first_tuple, second_tuple))


if __name__ == '__main__':
    main()