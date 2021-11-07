"""
Print the possible combinations upt k in lexicographical order
"""


from itertools import combinations as combo

S,K = map(str,input().split())
K = int(K)

li = ["".join(each) for _ in range(1,K+1) for each in combo(sorted(S),_)]
print(li)

#Comment out above two lines and below is another alternative without list comprehension
"""
    li = []
    for each in list(combo(S,_)):
        li.append(each)
    li = sorted([sorted(each) for each in li])
    print(li)
    for each in li:
        print("".join(each))
"""

