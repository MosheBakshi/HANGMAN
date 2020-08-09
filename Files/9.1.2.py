import os

# work on files with different actions as can be seen in main


def main():
    while True:
        path_input = input("Please enter a path to the file: ")
        action_input = input("""Please enter the action you wish for:
                                                    1) sort
                                                    2) rev
                                                    3) last
                                                    
                                                    please write it as written in menu option!
                                                    """)
        if action_input == 'sort':
            set_of_words = set(open(os.path.join(path_input), 'r').read().split())
            sorted_list = sorted(set_of_words)
            print(sorted_list)
        elif action_input == 'rev':
            # "C:\Users\shl\PycharmProjects\HANGMAN\Files\sampleFile.txt"
            revered_file_input = open(os.path.join(path_input), 'r')
            for line in revered_file_input.readlines():
                print(line[::-1])
        elif action_input == 'last':
            num_of_lines = input("""                Please enter number of lines: """)
            file_input = open(os.path.join(path_input), 'r').readlines()[-int(num_of_lines):]
            for line in file_input:
                print(line)


if __name__ == '__main__':
    main()