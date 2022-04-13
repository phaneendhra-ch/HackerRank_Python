#!/bin/python3

# This Comes Under Greedy Approach
"""
Problem Statement :

    Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. If Marc has eaten  cupcakes so far, after eating a cupcake with  calories he must walk at least  miles to maintain his weight.

Example : calorie = [5,10,7]

If he eats the cupcakes in the order shown, the miles he will need to walk are .

(2^0 x 5) + (2^1 x 10) + (2^2 x 7) = 5 + 20 + 28 = 53

This is not the minimum, though, so we need to test other orders of consumption. In this case, our minimum miles is calculated as .

(2^0 x 10) + (2^1 x 7) + (2^2 x 5) = 10 + 14 + 20 = 44(44 < 53 --> Greedy Approach)

Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles Marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.

"""
from itertools import permutations as p
#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    # Write your code here

    # Sort the list in descending order
    calorie = sorted(calorie,reverse = True)
    return sum(list(map(lambda each: (2**each[0])*(each[1]),list(enumerate(calorie)))))

    

    """

    Methods 2:
    
    combo = list(p(calorie))
    return min(list(map(lambda each: sum(list(map(lambda x:(2**x[0])*(x[1]),list(enumerate(each))))),combo)))

   """
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
