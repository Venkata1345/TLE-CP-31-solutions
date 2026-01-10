for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if (n-b)%2!=0:
        print('NO')
        continue 

    if a<=b:
        print("YES")
    
    else:
        if (n-a)%2==0:
            print('YES')
        else:
            print("NO")
