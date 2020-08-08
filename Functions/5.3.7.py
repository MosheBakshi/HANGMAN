def chocolate_maker(small, big, x):
    """ calculate if small or big pieces can create the relevant size of chocolate
    :param:small:big:x
    :type:int
    :return if can be created of small or big pieces
    :rtype:bool
    """
    if (x/big == 5) or (x/small == 1):
        return True
    elif x - small*1 - big*5 == 0:
        return True
    else:
        return False


print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))
print(chocolate_maker.__doc__)