def are_lists_equal(list1, list2):
    """
    :param list1:
    :param list2:
    :return: True if the lists contains the same values (even if not in the same order)
    :rtype: bool
    """

    # count_of_shared_elements = len(set(list1) & set(list2))     # CHECKING BY SET OF SHARED ELEMENTS
    # if count_of_shared_elements == len(list1):                  # NOT WORKS IN CASE SAME ELEMENT REPEAT IN LIST
    #     return True
    # else:
    #     return False

    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    return False


def main():
    print(are_lists_equal.__doc__)
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))


if __name__ == '__main__':
    main()