def longest(my_list):
    """
    :param my_list:
    :return: the longest string in the list
    """
    get_longest = sorted(my_list, key=len).pop()
    return get_longest


def main():
    print(longest.__doc__)
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))


if __name__ == '__main__':
    main()