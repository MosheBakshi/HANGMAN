def squared_numbers(start, stop):
    """
    :param start:
    :param stop:
    :return: List of all the numbers between start and stop squared
    """
    List = []
    i = start
    while i <= stop:
        List.append(i ** 2)
        i += 1
    return List


def main():
    print(squared_numbers.__doc__)
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))


if __name__ == '__main__':
    main()
