def distance(num1, num2, num3):
    """ CHECK IF ABSOLUTE DISTANCE IS CLOSE OR FAR AWAY {CLOSE = 1, FAR >=2}
    :param:num1:num2:num3
    :type:int
    :return if absolute distance
    :rtype:bool
    """
    if abs(num1 - num2) is 1 or abs(num1 - num3) is 1:
        return True
    elif abs(num1 - num2) >= 2:
        return True
    elif abs(num1 - num3) >= 2:
        return True
    elif abs(num2 - num3) >= 2:
        return True
    else:
        return False


print(distance(1, 2, 10))
print(distance(4, 5, 3))
