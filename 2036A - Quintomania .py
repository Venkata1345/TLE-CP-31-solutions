for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    flag=True
    for i in range(n-1):
        if abs(arr[i]-arr[i+1])!=5 and abs(arr[i]-arr[i+1])!=7:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
