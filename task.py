import math
import datetime


def areaFromRadius(radius):
    area = 3.14 * math.pow(radius, 2)
    return area


def getListEnds(list):
    result = [list[0], list[len(list) - 1]]
    return result


def dateDiff(date1, date2):
    return abs((date1 - date2).days)
