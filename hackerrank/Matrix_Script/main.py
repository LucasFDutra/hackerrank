import math
import os
import random
import re
import sys


def mount_the_word(matrix, n, m):
    string_matrix = ''
    for columns in range(m):
        for line in range(n):
            string_matrix += matrix[line][columns]
    return string_matrix

def matrix_decode(string_matrix):
    new_matrix = 'This$#is% Matrix#  %!'
    return re.sub(r'((?<=(\w))(\W+)(?=(\w+)))', ' ', string_matrix)

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    string_matrix = mount_the_word(matrix, n, m)
    print(matrix_decode(string_matrix))