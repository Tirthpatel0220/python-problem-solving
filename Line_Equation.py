'''
Line Equation
Problem Description:

You are given the slope m and the y-intercept b of a line, along with a value x. Your task is to calculate and return the value of y using the equation of a line in slope-intercept form:

y=mx+b

Input:

Three floating-point numbers: slope, intercept, and x.

Output:

A floating-point number representing the value of yyy corresponding to the given xxx.

Example:

Input: slope = 2, intercept = 3, x = 4
Output: 11.0

Input: slope = 1.5, intercept = -2, x = 2
Output: 1.0
'''


def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.

    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.

    Returns:
    float: The calculated value of y.
    """
    # Your code here
    y = (slope * x + intercept)
    return float(y)


print(calculate_y(2, 3, 4))