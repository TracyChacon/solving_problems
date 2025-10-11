#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER r
#  4. INTEGER_ARRAY t1
#  5. INTEGER_ARRAY t2
#  6. INTEGER_ARRAY t3
#

def solve(x: int, y: int, r: int, t1: list[int], t2: list[int], t3: list[int]):
    # Write your code here
    # Check if any triangle vertices lie on the circle
    

    print ("NO")

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()

    #     x = int(first_multiple_input[0])

    #     y = int(first_multiple_input[1])

    #     r = int(first_multiple_input[2])

    #     t1 = list(map(int, input().rstrip().split()))

    #     t2 = list(map(int, input().rstrip().split()))

    #     t3 = list(map(int, input().rstrip().split()))

    #     result = solve(x, y, r, t1, t2, t3)

    #     fptr.write(result + '\n')

    # fptr.close()

    print(solve(0, 0, 10, [10, 0], [15, 0], [15, 5]))
