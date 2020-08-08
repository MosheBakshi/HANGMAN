def inverse_dict(my_dict):
    """
    :param my_dict:
    :return: Inverse dictionary - every value becomes a key and holds list of key that had that value.
    """
    inverse_dictionary = {}
    for item in my_dict.items():
        if item[1] in inverse_dictionary:
            inverse_dictionary[item[1]].append(item[0])
        else:
            inverse_dictionary[item[1]] = []
            inverse_dictionary[item[1]].append(item[0])
    for value in inverse_dictionary.values():
        value.sort(key=sorted)
    return inverse_dictionary


def main():
    print(inverse_dict.__doc__)
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))


if __name__ == '__main__':
    main()
