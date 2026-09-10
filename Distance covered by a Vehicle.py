'''
Problem Description:

You are given the speed of a vehicle and the time it has traveled. Your task is to compute and return the distance traveled by the vehicle.

Formula:

To calculate the distance traveled by a vehicle:

Distance=Speed×Time

Input:

Two floating-point numbers, speed and time, representing the speed of the vehicle and the time it has been traveling.

Output:

A floating-point number representing the distance traveled.

Example:

Input: speed = 60, time = 2
Output: 120.0

Input: speed = 50.5, time = 1.5
Output: 75.75
'''


def calculate_distance(speed, time):
    """
    Function to calculate the distance traveled by a vehicle.

    Parameters:
    speed (float): The speed of the vehicle.
    time (float): The time the vehicle has traveled.

    Returns:
    float: The distance traveled by the vehicle.
    """
    # Your code here
    Distance = speed * time
    return float(Distance)


print(calculate_distance(60, 2))