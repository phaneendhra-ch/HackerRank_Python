"""
Sorting the list w.r.t  nested list value

5 3 --> 5 Rows , 3 Columns

10 2 5
7 1 0
9 9 9
1 23 12
6 5 9

1 -> sort wrt to 1 index


Output:

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

"""

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr =       sorted(arr,
                key = lambda arr:arr[k],
                reverse = False
                )
    for each in arr:
        print(*each)
