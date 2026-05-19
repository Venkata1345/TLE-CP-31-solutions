for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1):
        if arr[i]%2!=arr[i+1]%2:
            flag=True
        else:
            flag=False
            break
    if flag:
        print('YES')
    else:
        print('NO')
