
#
# Complete the 'beautifulBinaryString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING b as parameter.
#

def beautifulBinaryString(b):
    
    sub_str = "010"
    count = 0
    
    while True:
        flag = b.find(sub_str)
        
        if flag !=-1:
            count+= 1
            b = b[flag+len(sub_str):]
        else:
            break
    return count
            
if __name__ == '__main__':

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    print(str(result))
