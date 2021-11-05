# -*- coding:utf-8 -*-
"""
Author: mohanren
Date: 05//11//2021//
"""
from random import randint as ri


def shoot_player():
    while True:
        # the first player's turn
        shoot1 = ri(1, 5)
        if shoot1 == 1:
            return "a"
        # the second player's turn
        shoot2 = ri(1, 5)
        if shoot2 == 1:
            return "b"
        # the third player's turn
        shoot3 = ri(1, 5)
        if shoot3 == 1:
            return "c"
        else:
            continue


def main():
    player1 = 0.0
    player2 = 0.0
    player3 = 0.0
    total_round = 100000
    for i in range(0, total_round):
        winner = shoot_player()
        if winner == "a":
            player1 += 1.0
        elif winner == "b":
            player2 += 1.0
        elif winner == "c":
            player3 += 1.0

    pro_p1 = float(player1) / float(total_round)
    pro_p2 = float(player2) / float(total_round)
    pro_p3 = float(player3) / float(total_round)

    # Output the results
    print("The probability for player 1 to win is :" + str(pro_p1*100) + "%")
    print("The probability for player 2 to win is :" + str(pro_p2 * 100) + "%")
    print("The probability for player 3 to win is :" + str(pro_p3 * 100) + "%")


if __name__ == "__main__":
    main()
