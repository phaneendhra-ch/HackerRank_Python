from collections import OrderedDict

"""
With the help of OrderedDict : the list can remove the duplicate elements
                                without changing the order


Input :

s = 'AABCAAADA'
k = 3  # break the string at regular intevals of 3

Output:

# prints the substrings by removing duplicate characters without changing the
order

AB
CA
AD

"""

def merge_the_tools(string, k):
    li = [string[each:each+k] for each in range(0,len(string),k)]
    for each in range(len(li)):
        li[each] = list(OrderedDict.fromkeys(li[each]))


    for each in li:
        for each_ind in range(len(each)):
            print(f"{each[each_ind]}",end="")
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
