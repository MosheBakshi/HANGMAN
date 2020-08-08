from Subject1 import *
picture1 = """
    x-------x
    """
picture2 = """
    x-------x
    |
    |
    |
    |
    |
    """
picture3 = """
    x-------x
    |       |
    |       0
    |
    |
    |
    """
picture4 ="""
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """
picture5 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """
picture6 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """
picture7 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
HANGMAN_PHOTOS = {'1': picture1, '2': picture2, '3': picture3, '4': picture4, '5': picture5, '6': picture6,
                  '7': picture7}


def print_hangman(num_of_tries):
    """
    :param num_of_tries:
    :return: None
    """
    print(HANGMAN_PHOTOS[str(num_of_tries)])


def main():
    num_of_tries = 6
    print_hangman(num_of_tries)


if __name__ == '__main__':
    main()