for _ in range(int(input())):
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    c =0
    for i in s:
        if len(i)<=m:
            c+=1
            m = m - len(i) 
        else:
            break 
    print(c)
