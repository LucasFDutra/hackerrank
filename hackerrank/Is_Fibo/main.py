import os
import sys

def solve(n):
    v1 = 0
    v2 = 1
    if n == 1:
        return 'IsFibo'
    while (v2 < n):
        tmp = v1 + v2
        v1 = v2
        v2 = tmp
        print(v2)
        if v2 == n:
            return 'IsFibo'
    return 'IsNotFibo'

if __name__ == "__main__":
    print(solve(25))