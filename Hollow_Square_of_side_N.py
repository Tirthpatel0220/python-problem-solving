# Hollow Square of side 'N'
# Problem Description:
#
# You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).

#example
# Input: 3
# Output: ['***', '* *', '***']
#
# Input: 5
# Output: ['*****', '*   *', '*   *', '*   *', '*****']

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    if n == 1:
        return ["*"]

    make_star = "*" * n
    result = [make_star] * n

    # Handle middle rows only if n > 2
    if n > 2:
        result[1:-1] = ["*" + " " * (n - 2) + "*"] * (n - 2)

    return result


print(generate_hollow_square(3))