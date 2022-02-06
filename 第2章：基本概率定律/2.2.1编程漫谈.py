# -*- coding:utf-8 -*-
"""
Author: mohanren
Date: 06//02//2022//
"""
from math import sqrt

def sumfoursquares(m):
    count = 0
    list = []  # Store the valid 4-element-tuple
    root = int(sqrt(m))
    for a in range(root):
        for b in range(min(a, int(sqrt(m-a**2)))):
            for c in range(min(b, int(sqrt(m-a**2-b**2)))):
                d = sqrt(m-a**2-b**2-c**2)
                if (d>=0) and (d<=c) and (d.is_integer()):
                    count += 1
                    list.append([a, b, c, int(d)])
    print("-----------------------Better Case------------------------")
    print("The number of representations of ", str(m), " as a sum of four squares is ", str(count))
    print(list)


def worse(m):
    count = 0
    list = []
    for a in range(int(sqrt(m))):
        for b in range(a):
            for c in range(b):
                for d in range(c):
                    if m == a**2 + b**2 + c**2 + d**2:
                        count += 1
                        list.append([a, b, c, d])
    print("-----------------------Worse Case------------------------")
    print("The number of representations of ", str(m), " as a sum of four squares is ", str(count))
    print(list)


if __name__ == "__main__":
    num = 20000
    sumfoursquares(num)
    worse(num)