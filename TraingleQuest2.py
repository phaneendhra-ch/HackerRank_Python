"""
Input:
5

Output:

1
121
12321
1234321
123454321

"""

count,val = 1,10
for i in range(1,int(input())+1): 
    print(count*count)
    count,val = count%val + val, val*10
