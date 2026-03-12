for _ in range(int(input())):
    n,a,b = map(int, input().split())
    s= input()
    x,y = 0,0
    met = False
    for _ in range(100):
        for i in range(n):
            if s[i] == 'N':
                y+=1
            elif s[i] =='E':
                x+=1
            elif s[i] == 'S':
                y-=1 
            elif s[i] ++ 'W':
                x-=1 
            if x==a and y==b:
                met = True
                break

        if met:
            break
    if met:
        print('YES')
    else:
        print('NO')
