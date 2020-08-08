def last_early(my_str):
    """ CHECK IF ABSOLUTE DISTANCE IS CLOSE OR FAR AWAY {CLOSE = 1, FAR >=2}
    :param:my_str
    :type:string
    :return if letter exists not just in the end
    :rtype:bool
    """
    last_letter = my_str[-1].lower()
    return last_letter in my_str[:len(my_str)-1].lower()


print(last_early("happy birthday"))
print(last_early("best of luck"))
print(last_early("Wow"))
print(last_early("X"))
