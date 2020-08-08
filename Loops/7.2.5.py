def sequence_del(my_str):
    """
    :param my_str:
    :return: String made of the received string, without repeat of characters, SssHH -> Ssh
    """
    new_str = my_str[0]
    for chars in my_str:
        if new_str[len(new_str)-1] != chars:
            new_str = new_str + chars
    return new_str


def main():
    print(sequence_del.__doc__)
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))


if __name__ == '__main__':
    main()