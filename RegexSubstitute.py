"""

Here Substitute the string

    -> ' && ' with ' and '
    -> ' || ' with ' or '

Author : Phaneendhra

"""

import re

N = int(input())
str_ = ""
for each in range(N):
    c = input()
    while (' && ' in c):                    # iterate while for one or more occurences in same line
        c = re.sub(' \&\& ',' and ',c)              # Substitute && with and,
                                                    # if string is &&& then it remains same

    while(' || ' in c):                     # if string is &&& then it remains same
        c = re.sub(' \|\| ',' or ',c)               # Substitute || with or,
                                                    # if string is ||| then it remains same

    str_+=c+'\n'                                    # append the updated string

print(str_)                                         # print the string after replacing with 'and' and 'or'
