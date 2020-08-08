def format_list(my_list):
    """
    :param my_list:
    :type: list
    :return: list separated with ', ' & before the last item add the word 'and '
    :rtype: list
    """
    new_list = ', '.join(my_list[0:len(my_list)-1:2]) + " and " + my_list[len(my_list)-1]
    return new_list


def main():
    print(format_list.__doc__)
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    print(format_list(my_list))


if __name__ == '__main__':
    main()

