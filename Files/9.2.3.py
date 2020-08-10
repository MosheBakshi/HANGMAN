import os


def who_is_missing(file_name):
    """
    :param file_name:
    :return: return int(missing num) and writing it to another file named found.txt
    """
    COMMA = ","
    list_of_nums = []
    missing_nums = []
    file_input = open(file_name, "r")
    lines = file_input.read()
    for i in range(lines.count(COMMA)+1):
        num = lines.split(COMMA)[i]
        list_of_nums.append(int(num))
    list_of_nums = set(list_of_nums)
    print("List of nums: ", list_of_nums)
    file_output = open(os.getcwd() + r"\found.txt", "w")
    for item in range(1,max(list_of_nums)):
        if item not in list_of_nums:
            missing_nums.append(item)
    file_output.write(str(missing_nums))
    return missing_nums


def main():
    print(who_is_missing(os.getcwd()+r"\findMe.txt"))


if __name__ == '__main__':
    main()