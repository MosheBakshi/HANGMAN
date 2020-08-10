import os


def choose_word(file_path, index):
    """
    :param file_path:
    :param index:
    :return: tuple (num of words without duplicates, the word of the given index in the file
    """
    file_input = open(file_path, "r")
    count_of_words = len(set(file_input.read().split(" ")))
    file_input.seek(0)
    lines = file_input.read().split(" ")
    list_of_words = []
    for item in lines:
        list_of_words.append(item)
    relevant_tuple = (count_of_words, list_of_words[index % len(list_of_words)-1])
    return relevant_tuple


def main():
    print(choose_word(os.getcwd() + r"\words.txt", 3))
    print(choose_word(os.getcwd() + r"\words.txt", 15))


if __name__ == '__main__':
    main()
