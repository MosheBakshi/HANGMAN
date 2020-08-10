import os


def my_mp3_playlist(file_path):
    """
    :param file_path:
    :return: tuple (The name of longest song, count songs, most appeared singer)
    """
    file_input = open(file_path, "r")
    lists = file_input.read().split("\n")
    lists_splited = []
    for item in lists:
        item = item.split(';')
        lists_splited.append(item)
    song_name = longest_song(lists_splited)
    counter_songs = count_songs(lists_splited)
    appeared_singer = most_appeared_singer(lists_splited)
    the_tuple = (song_name, counter_songs, appeared_singer)
    return the_tuple


def count_songs(playlist):
    list_of_song = []
    for item in playlist:
        list_of_song.append(item[0])
    list_of_song = list(set(list_of_song))
    return len(list_of_song)


def most_appeared_singer(playlist):
    list_of_song = []
    max_appears = 0
    singer_name = ""
    for item in playlist:
        list_of_song.append(item[1])
    counter = list(set(list_of_song))
    for item in counter:
        if list_of_song.count(item) > max_appears:
            max_appears = list_of_song.count(item)
            singer_name = item
    return singer_name


def longest_song(playlist):
    max_minute = 0
    max_second = 0
    song_name = ""
    for item in playlist:
        if int(str(item[2]).split(':')[0]) > max_minute:
            max_minute = int(str(item[2]).split(':')[0])
            song_name = str(item[0])
        elif int(str(item[2]).split(':')[0]) == max_minute and \
                int(str(item[2]).split(':')[2] + str(item[2]).split(':')[3]) > max_second:
            max_second = int(str(item[2]).split(':')[2] + str(item[2]).split(':')[3])
            song_name = str(item[0])
    return song_name


def main():
    print(my_mp3_playlist(os.getcwd() + r"\mp3list.txt"))


if __name__ == '__main__':
    main()
