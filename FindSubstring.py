"""

In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC  -->string
CDC  -->substring

Sample Output
2

"""

import re
def count_substring(string, sub_string):
    count = 0
    start,end = 0,len(string)
    while True:
        string = string[start:end]  # iterating from start to end, default 0,0
        c = re.search(sub_string,string) #if substring exists,we will get start,end index
        if c!= None:   # if substring doesnt exists then it returns None
            count +=1 #incremenet count
            start,end = (c.span()[-1])-1,len(string) # update new start index
        else:
            break 
    return (count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)