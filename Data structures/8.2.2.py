def sort_prices(list_of_tuples):
    """
    :param list_of_tuples:
    :return: New tuples list sorted by prices high to low
    """
    new_list = sorted(list_of_tuples, key=lambda x: (x[1]), reverse=True)
    return new_list


def main():
    print(sort_prices.__doc__)
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))


if __name__ == '__main__':
    main()