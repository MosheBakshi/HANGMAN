import os
import time

from colorama import Fore, Back, Style


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
picture4 = """
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
    print(Fore.LIGHTYELLOW_EX + HANGMAN_PHOTOS[str(num_of_tries)], '\n')
    time.sleep(2)


def check_win(secret_word, old_letters_guessed):
    """
    :param secret_word:
    :param old_letters_guessed:
    :return: returns True if player guessed all the letters of the hidden word
    """
    for letter in secret_word:  # checks if all letters exposed
        if letter not in old_letters_guessed:
            return False
    return True


def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word:
    :param old_letters_guessed:
    :return: String of the hidden word except the letters already guessed
    """
    new_string = ""
    for letter in secret_word:  # show the sectors where the letter belongs and leave '_' where not exposed
        if letter in old_letters_guessed:
            new_string = new_string + letter
        else:
            new_string = new_string + ' _ '
    return new_string


def check_valid_input(the_guess):
    """
    :param: the_guess:
    :type: string
    :return: if valid guess for the game
    :rtype: bool
    """

    ENGLISH_FLAG = the_guess.isascii()
    LENGTH_FLAG = len(the_guess) < 2
    SIGNS_FLAG = the_guess.isalpha()

    if (LENGTH_FLAG is False and  # IN CASE MORE THAN 1 LETTER BUT ELSE IS FINE
            ENGLISH_FLAG is True and
            SIGNS_FLAG is True):
        return False
    elif (LENGTH_FLAG is True and  # NOT IN ENGLISH AND SIGNS BUT IN LENGTH
          SIGNS_FLAG is False):
        return False
    elif (ENGLISH_FLAG is False or  # SAME AS UP BUT LONG STRING
          (SIGNS_FLAG is False and
           LENGTH_FLAG is False)):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    :param: letter_guessed: old_letters_guessed:
    :type: string: list
    :return: if valid guess or already exists in the game
    :rtype: bool
    """

    ENGLISH_FLAG = letter_guessed.isascii()
    LENGTH_FLAG = len(letter_guessed) < 2
    SIGNS_FLAG = letter_guessed.isalpha()

    if (LENGTH_FLAG is False and  # IN CASE MORE THAN 1 LETTER BUT ELSE IS FINE
            ENGLISH_FLAG is True and
            SIGNS_FLAG is True):
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    elif (LENGTH_FLAG is True and  # NOT IN ENGLISH AND SIGNS BUT IN LENGTH
          SIGNS_FLAG is False):
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    elif (ENGLISH_FLAG is False or  # SAME AS UP BUT LONG STRING
          (SIGNS_FLAG is False and
           LENGTH_FLAG is False)):
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        print('X')
        print('->'.join(old_letters_guessed))
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        old_letters_guessed.sort()
        return True


def choose_word(file_path, index):
    """
    :param file_path:
    :param index:
    :return: tuple (num of words without duplicates, the word of the given index in the file
    """
    file_input = open(file_path, "r")
    file_input.seek(0)
    lines = file_input.read().split(" ")
    list_of_words = []
    for item in lines:
        list_of_words.append(item)
    return list_of_words[int(index) % len(list_of_words)-1]


def print_logo(choice):
    if choice == '1':
        print(Fore.LIGHTRED_EX + """
             _    _                                         
            | |  | |                                        
            | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
            |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | |  | | (_| | | | | (_| | | | | | | (_| | | | |
            |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                 __/ |                      
                                |___/
                """)
    else:
        print(Fore.LIGHTBLUE_EX + """
             _    _                                         
            | |  | |                                        
            | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
            |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | |  | | (_| | | | | (_| | | | | | | (_| | | | |
            |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                 __/ |                      
                                |___/
                """)
    time.sleep(2)
    return None


def main():
    file_path = ""
    num_of_tries = 1
    old_letters_guessed = []
    print(Fore.WHITE + "Please choose by the number:\n",
          "                ", Fore.RED + '1) Your file path.\n',
          "                ", Fore.BLUE + '2) The project directory file.\n\n',
          "                ", Fore.WHITE + 'Write' + Fore.RED + ' 1' + Fore.LIGHTCYAN_EX + ' or ' + Fore.BLUE + '2')
    choice = input(Fore.WHITE + "                Your Choice: ")
    if choice != '1' and choice != '2':
        main()
    elif choice == '1':
        file_path = input("Enter file path: ")
    elif choice == '2':
        file_path = os.getcwd() + r"\words.txt"
    index = input("Enter index: ")
    chosen_word = choose_word(file_path, index)
    print_logo(choice)
    print(Fore.LIGHTGREEN_EX + "Let's Start!!!")
    print_hangman(str(num_of_tries))
    print(show_hidden_word(chosen_word, old_letters_guessed) + '\n\n')
    while check_win(chosen_word, old_letters_guessed) is False:
        guess = input("Enter a guess: ")
        while not try_update_letter_guessed(guess, old_letters_guessed):    # in case bad letter
            num_of_tries += 1
            print(Fore.RED + ':(')
            time.sleep(2)
            print_hangman(str(num_of_tries))
            print(show_hidden_word(chosen_word, old_letters_guessed) + '\n\n')
            guess = input("Enter a guess: ")
            if num_of_tries == 6:
                print(Fore.RED + 'LOSE... :(')
                time.sleep(2)
                exit()
        print_hangman(str(num_of_tries))
        print(show_hidden_word(chosen_word, old_letters_guessed) + '\n\n')
    print(Fore.LIGHTGREEN_EX + 'WIN!!! :)')
    time.sleep(2)
    exit()


if __name__ == '__main__':
    main()
