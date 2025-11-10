for _ in range(int(input())):
    n,s,m=map(int,input().split())
    tb=[]
    for i in range(n):
        l,r=map(int,input().split())
        tb.append((l,r))
    
    if tb[0][0]-0>=s or m-tb[n-1][1]>=s:
        print('YES')
        continue
    
    for j in range(n-1):
        if (tb[j+1][0]-tb[j][1])>=s:
            print('YES')
            break
    
    print('NO')
