from itertools import groupby
from nltk.corpus import words


def sort_anagrams(list_of_strings):
    """
    :param list_of_strings:
    :return: list of lists contains words are anagram of each other
    """
    output = [list(group) for key, group in groupby(sorted(list_of_strings, key=sorted), sorted)]
    return output


def main():
    print(sort_anagrams.__doc__)
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))


if __name__ == '__main__':
    main()