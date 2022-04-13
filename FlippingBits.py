
#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    # (1 << 32)-1 = pow(2,32) - 1
    # All bits are set here for a 32 bit number
    
    return n ^ ((1<<32)-1)
if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(str(result) + '\n')
