from math import pi


def calc_area(radius):
    area = pi * radius ** 2
    return area


def first_last(list):
    result = [list[0], list[-1]]
    return result


def calc_days(fdate, ldate):
    days = ldate - fdate
    return days
