for _ in range(int(input())):
    x,y,a = map(int, input().split())
    s=x+y
    r = a%s 
    if x > r:
        print('NO')
    else:
        print('YES')
