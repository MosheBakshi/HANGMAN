def seven_boom(end_number):
    """
    :param end_number:
    :return: List in length of end_number and contains the word "boom" if number%7 == 0 or number contains 7
    """
    boom = []
    for i in range(end_number+1):
        if i % 7 == 0 or '7' in str(i):
            boom.append("BOOM")
        else:
            boom.append(i)
    return boom


def main():
    print(seven_boom.__doc__)
    print(seven_boom(17))


if __name__ == '__main__':
    main()