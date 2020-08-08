import filecmp
import os


def are_files_equal(file1, file2):
    """
    :param file1:
    :param file2:
    :return: bool - if files content is equal
    """
    file1_input = open(os.getcwd() + file1, "r")
    file2_input = open(os.getcwd() + file2, "r")
    line1 = file1_input.readlines()
    line2 = file2_input.readlines()
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            file1_input.close()
            file2_input.close()
            return False
    file1_input.close()
    file2_input.close()
    return True
    # return filecmp.cmp(os.getcwd() + r"\file1", os.getcwd() + r"\file2") # ANOTHER EASY WAY OF COMPARING


def main():
    print(are_files_equal(r"\file1",
                          r"\file2"))


if __name__ == '__main__':
    main()