

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    s_count,t_count = 0,0
    len_s,len_t = len(s),len(t)
    
    while (s[s_count] == t[t_count]) and s[s_count] and t[t_count]:
        if (s_count+1 == len_s or t_count+1 == len_t):
            break
        
        s_count+=1
        t_count+=1
        
    
    if ((len_s - s_count) + (len_t - t_count) <=k):
        return "Yes"
    else:
        return "No"
    

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result + '\n')

