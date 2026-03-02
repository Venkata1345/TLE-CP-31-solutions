for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = False
    zero= arr.count(0)
    if zero==0:
        print('YES')
    else:
        for i in range(n-1):
            if arr[i]==0 and arr[i+1]==0:
                flag = True
                break
    
        if flag:
            print('YES')
        else:
            print('NO')
