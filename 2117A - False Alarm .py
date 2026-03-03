for _ in range(int(input())):
    n,x = map(int, input().split())
    arr = list(map(int, input().split()))
    first_one = -1
    last_one = -1
    for i in range(n):
        if arr[i]==1:
            if first_one == -1:
                first_one = i
            last_one = i
    if first_one == -1:
        print("YES")
    else:
        rest = last_one - first_one +1
        if rest<=x:
            print('YES')
        else:
            print('NO')
