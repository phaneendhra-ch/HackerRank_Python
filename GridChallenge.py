#!/bin/python3
"""
Problem Statement:

    Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

    Example

    The grid is illustrated below.

        a b c
        a d e
        e f g
    
    The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.


"""
#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    
    for i in range(1,len(grid)):
        for j in range(len(grid)):
            if j==0:
                hold = grid[j][i-1]
                
            elif hold <= grid[j][i-1]:
                hold = grid[j][i-1]
                
            else:
                return "NO"
    return "YES"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        print(result + '\n')
