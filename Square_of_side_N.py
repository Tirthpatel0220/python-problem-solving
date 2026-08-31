# Square of side 'N'
# Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings.

# Example:
#
# Input: 3
# Output: ['***', '***', '***']
#
# Input: 5
# Output: ['*****', '*****', '*****', '*****', '*****']

def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    first_is = n * "*"
    for i in first_is:
        list = [first_is] * n
        return list


print(generate_square(5))