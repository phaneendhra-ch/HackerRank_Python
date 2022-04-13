#!/bin/python3

#This Problem comes under Greedy Section

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr = sorted(arr,reverse = False)
    li = []
    # weneed to find the subsets
    # n-k+1 -->total
    
    for i in range(n-k+1):
        #each subset can be found using 
        diff_subset = arr[i+k-1] - arr[i]   # contains k elements of ith subset
        li.append(diff_subset)

    return min(li)
if __name__ == '__main__':

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(str(result) + '\n')
