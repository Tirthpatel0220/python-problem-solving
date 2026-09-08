'''
Problem Description:

You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', where the first row contains n stars, while the inner rows contain a star at the beginning and end, with spaces in between. The triangle should be left-aligned.

Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string represents a row in the hollow inverted right-angled triangle.



Example:

Input: 4
Output: ['****', '* *', '**', '*']

Input: 5
Output: ['*****', '*  *', '* *', '**', '*']
'''


#The way i have solved this pattern problem but this is not efficient by the way so i learned also second type of code.
# def generate_hollow_right_angled_triangle(n):
#     """
#     Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
#     """
#     ls = []
#
#     for i in range(1, n + 1):
#         if i == 1 or i == 2 or i == n:
#             ls.append("*" * i)
#         else:
#             for j in range(1, 2):
#                 ls.append("*" + " " * (i - 2) + "*")
#
#     return ls
#
# print(generate_hollow_right_angled_triangle(5))

'''
This is the code which i learned because my code has two for loop so it is not efficient so learned this so prefer this logic.
'''

def generate_hollow_right_angled_triangle(n):
    ls = []

    for i in range(1, n + 1):
        if i == 1:
            ls.append("*")
        elif i == n:
            ls.append("*" * i)
        else:
            ls.append("*" + " " * (i - 2) + "*")

    return ls

print(generate_hollow_right_angled_triangle(5))