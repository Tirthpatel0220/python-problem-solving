'''
Number of Rounds of Lift
Problem Description:

You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. All people want to go from the ground floor to the top floor. Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.

Input:

Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people the lift can carry in one round.

Output:

An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.

Example:

Input: n = 10, capacity = 3
Output: 4

Input: n = 7, capacity = 4
Output: 2

'''
def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    """
    estimate = n / capacity
    estimate_round = n // capacity

    remaining = n % capacity

    if remaining != 0:
        estimate_round += 1
    elif remaining == 0:
        estimate_round += 0

    return estimate_round


print(calculate_lift_rounds(7, 4))