def extend_list_x(list_x, list_y):
    """
    :param list_x:
    :param list_y:
    :type:list:list:
    :return: list_x after list_y combined in
    """
    list_x[:0] = list_y
    return list_x

def main():
    print(extend_list_x.__doc__)
    x = [4, 5, 6]
    y = [1, 2, 3]
    print(extend_list_x(x, y))


if __name__ == '__main__':
    main()