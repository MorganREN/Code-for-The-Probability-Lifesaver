# -*- coding:utf-8 -*-
"""
Author: mohanren
Date: 05//11//2021//
"""
from random import randint as ri


def create_birth(n):
    room = []
    for i in range(0, n):
        birth = ri(1, 366)
        # print(birth)
        room.append(birth)
        i += 1
    return room


def find_share(room):
    found = False
    j = 1
    for i in range(0, len(room)):
        for j in range(i+1, len(room)):
            if room[i] == room[j]:
                found = True
                return found
            j += 1
        i += 1
    return found


def main():
    n = int(input("How many people should in one room? \n"))
    total = 10000.0  # To get a float answer, we need to set this variable and the next one as float
    share = 0.0
    for i in range(int(total)):
        room = create_birth(n)
        if find_share(room):
            print(share)
            share += 1.0
        else:
            continue
    share_probability = share / total
    print("The probability for " + str(n) + " people in one room has the same birth is: " + str(share_probability*100.0) + "%")


if __name__ == "__main__":
    main()
