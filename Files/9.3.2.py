import os


def my_mp4_playlist(file_path, new_song):
    """
    :param file_path:
    :param new_song:
    :return: None - just output to file the new song name on the 3th place in the right format
    """
    file_input = open(file_path, "r")
    lists = file_input.read().split("\n")
    lists_splitter = []
    lists_to_output = []
    file_input.seek(0)
    first_char = file_input.read(1)
    for item in lists:
        item = item.split(';')
        lists_splitter.append(item)
    if not first_char:
        lists_to_output = ["\n", "\n", new_song]
        file_input.close()
    else:
        lists_splitter[2][0] = new_song
        file_input.close()
        for item in lists_splitter:
            item[len(item)-1] = '\n'
            lists_to_output.append(';'.join(item))
    file_input = open(file_path, "w")
    for item in lists_to_output:
        file_input.write(item)
    file_input.close()


def main():
    my_mp4_playlist(os.getcwd() + r"\mp3list.txt", "Python Love Story")
    file_input = open(os.getcwd() + r"\mp3list.txt", "r")
    print(file_input.read())


if __name__ == '__main__':
    main()