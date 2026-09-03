'''
You are given an integer n. Your task is to return an inverted right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.

Output:

A list of strings where each string is a row of '*' characters that decreases in length from n to 1.



Example:

Input: 3
Output: ['***', '**', '*']

Input: 5
Output: ['*****', '****', '***', '**', '*']
'''


def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    ls = []
    for i in range(n, 0, -1):
        ls.append(i * "*")
    return ls


print(generate_inverted_triangle(3))