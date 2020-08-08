def is_greater(my_list, n):
    """
    :param my_list:
    :param n:
    :return: List of all numbers greater than 'n'
    """
    List = []
    for num in my_list:
        if num > n:
            List.append(num)
    return List


def main():
    print(is_greater.__doc__)
    print(is_greater([1, 30, 25, 60, 27, 28], 28))


if __name__ == '__main__':
    main()