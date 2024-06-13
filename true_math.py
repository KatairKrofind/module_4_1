from math import inf
def divide():
    first = int(input())
    second = int(input())
    if second == 0:
        print(inf)
    else:
        print(first/second)