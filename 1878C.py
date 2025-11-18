for _ in range(int(input())):
    n,k,x=map(int,input().split())
    smallest_sum=(k*(k+1))//2
    largest_sum=(n*(n+1)//2)-(((n-k)*(n-k+1))//2)
    if x>=smallest_sum and x<=largest_sum:
        print('YES')
    else:
        print('NO')
