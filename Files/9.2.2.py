import os


def copy_file_content(source, destination):
    """
    :param source:
    :param destination:
    :return:None
    # copying source file content to the destination
    """
    file2 = open(destination, "r")
    print("Before copy:\n", file2.read())
    file2.close()
    file1 = open(source, "r")
    file2 = open(destination, "w")
    for line in file1.readlines():
        file2.write(line)
    file2.close()
    file2 = open(destination, "r")
    print("After copy:\n", file2.read())


def main():
    copy_file_content(os.getcwd() + r"\file1", os.getcwd() + r"\file2")


if __name__ == '__main__':
    main()