for _ in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        print('-1')
        continue

    if x>y:
        if y==0:
            print('1')
        else:
            if x>=4 and y>=2 and (x-y)>=2:
                print('3')
            else:
                print('-1')
    else:
        if x>=1 and y>=2 and (y-x)>=1:
            print('2')
        else:
            print('-1')
