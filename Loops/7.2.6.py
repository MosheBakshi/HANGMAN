import time


def menu_for_main(products_str):
    """
    :param products_str:
    :return: None
    """
    products_str = sequence_del(products_str)
    while True:
        print(""" 
            Menu: 
                1) Print the list.
                2) Count amount of products overall.
                3) -> Check if product in the list.
                4) ? Amount of specific product in the list.
                5) - Delete product of the list.
                6) + Add product to the list.
                7) Print illegal products (all names shorter than 3 or contains illegal chars)
                8) Hide all duplicates
                9) EXIT""")
        choice = input("SELECT ACTION: ")
        if choice == '1':
            print("""
            
            """, products_str)
        elif choice == '2':
            print(len(products_str))
        elif choice == '3':
            product_to_check = input("Please enter the name of the product: ")
            print(products_str.__contains__(product_to_check))
        elif choice == '4':
            product_to_check = input("Please enter the name of the product: ")
            print("The amount of ", product_to_check, "is: ", products_str.count(product_to_check))
        elif choice == '5':
            product_to_check = input("Please enter the name of the product: ")
            products_str.remove(product_to_check)
            print(product_to_check, " has removed from the list!")
            print(products_str)
        elif choice == '6':
            product_to_check = input("Please enter the name of the product: ")
            products_str.append(product_to_check)
            print(product_to_check, " has added to the list!")
            print(products_str)
        elif choice == '7':
            print("Illegal products are: ", is_valid_product(products_str))
        elif choice == '8':
            temp_list = list(set(products_str))
            print("No duplicates list: ", temp_list)
        elif choice == '9':
            print("GOOD BYE!")
            break
        time.sleep(2)
    return None


def is_valid_product(the_list):
    """
    :param: the_list:
    :type: list
    :return: list of illegal products
    :rtype: list
    """
    illegal_list = []
    for product in the_list:
        length_of_name = len(product) > 2
        only_letters = str(product).isalpha()
        if not length_of_name and not only_letters:
            illegal_list.append(product)
    return illegal_list


def sequence_del(my_str):
    """
    :param my_str:
    :return: List made of the received string of all the products the user entered
    """
    List = list(my_str.split(','))
    print(List)
    return List


def main():

    user_string = input("Please enter list of products separated by ',' without spaces: ")
    menu_for_main(user_string)


if __name__ == '__main__':
    main()