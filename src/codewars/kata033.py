"""
5 kyu - Greed is Good

Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point

 A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

 Note: your solution must not modify the input list.
"""


def score(dice: list):
    dict_dice = {}
    for num in dice:
        if num in dict_dice:
            dict_dice[num] += 1
        else:
            dict_dice[num] = 1

    total_score = 0

    for num, count in dict_dice.items():
        if count >= 3:
            if num == 1:
                total_score += 1000
            else:
                total_score += num * 100
            dict_dice[num] -= 3

    if 1 in dict_dice:
        total_score += dict_dice[1] * 100
    if 5 in dict_dice:
        total_score += dict_dice[5] * 50

    return total_score


print(score([4, 4, 4, 3, 3]))
