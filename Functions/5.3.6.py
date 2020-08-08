def filter_teens(a=13, b=13, c=13):
    """ fix teen age in case of 13,14,17,18,19 and sum them all
    :param:a:b:c
    :type:int
    :return sum of ages
    :rtype: int
    """
    if 13 <= a <= 14 or 17 <= a <= 19:
        a = fix_age(a)
    if 13 <= b <= 14 or 17 <= b <= 19:
        b = fix_age(b)
    if 13 <= c <= 14 or 17 <= c <= 19:
        c = fix_age(c)
    return a + b + c





def fix_age(age):
    """ fix teen age in case of 13,14,17,18,19 to 0
    :param:age
    :type:int
    :return set to zero
    :rtype: int
    """
    age = 0
    return age


print(filter_teens())
print(filter_teens(1, 2, 3))
print(filter_teens(2, 13, 1))
print(filter_teens(2, 1, 15))
