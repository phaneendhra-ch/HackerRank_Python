"""
Hacker Rank Problem Solving 

A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return .

    Example

    The person can buy a , or a . Choose the latter as the more expensive option and return .

    Function Description

    Complete the getMoneySpent function in the editor below.

    getMoneySpent has the following parameter(s):

    int keyboards[n]: the keyboard prices
    int drives[m]: the drive prices
    int b: the budget

    Returns

    int: the maximum that can be spent, or  if it is not possible to buy both items

"""

def getMoneySpent(keyboards, drives, b):

    #Method 1:
    c = list(map(lambda x:max(x) if x!=[] else -1,list(map(lambda x:list(filter(lambda z:z<b,map(lambda y:y+x,drives))),keyboards))))
    return sorted(c) if c!=[] else -1

    """
    #Method 2:
    c = sorted(list(map(lambda x:max(x) if x!=[] else -1,list(map(lambda x:list(filter(lambda z:z<=b,map(lambda y:y+x,drives))),keyboards)))),reverse=True)
    return c[0] if c!=[] else -1
    """
    # Can use either methods

if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')
