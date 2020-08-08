import time
from datetime import date


def menu_for_main(my_dict):
    """
    :param my_dict:
    :return: None
    """
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Auguste', 'September', 'October',
                  'November', 'December']
    while True:
        print(""" 
            Menu: 
                1) Print the last name.
                2) Print the birth month.
                3) Print the number of hobbies.
                4) Print the last hobby.
                5) Add the hobby "Cooking" to hobbies list.
                6) Convert the birth date into tuple and print it.
                7) Add new key of "Age" and print it.
                8) EXIT""", '\n')
        choice = input("SELECT ACTION: ")
        if choice == '1':
            print("The last name is: ", my_dict['last_name'])
        elif choice == '2':
            print("The birth month is:", my_dict['birth_date'].split('.')[1:2], ', also known as: ',
                  month_list[int(my_dict['birth_date'].split('.')[1:2][0])-1])
        elif choice == '3':
            print("Number of hobbies: ", len(my_dict['hobbies']))
        elif choice == '4':
            print("The last hobby: ", my_dict['hobbies'][-1])
        elif choice == '5':
            my_dict['hobbies'].append("Cooking")
            print("The edited list:")
            for value in my_dict['hobbies']:
                print("             ", value)
        elif choice == '6':
            date_tuple = (int(my_dict['birth_date'].split('.')[0:1][0]), int(my_dict['birth_date'].split('.')[1:2][0])
                          , int(my_dict['birth_date'].split('.')[2]))
            print(date_tuple)
        elif choice == '7':
            my_dict['Age'] = date.today().year - int(my_dict['birth_date'].split('.')[2])
            print("The age is:", my_dict['Age'])
        elif choice == '8':
            print("GOOD BYE!")
            break
        time.sleep(2)
    return None


def main():
    list_of_hobbies = ["Sing", "Compose", "Act"]
    my_dict = {"first_name": "Mariah", "last_name": "Carey", "birth_date": "27.03.1970", "hobbies": list_of_hobbies}
    menu_for_main(my_dict)


if __name__ == '__main__':
    main()