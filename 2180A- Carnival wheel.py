for _ in range(int(input())):
    l,a,b=map(int,input().split())
    mx=0
    curr_max=a
    for i in range(l):
        if curr_max>mx:
            mx=curr_max 
        curr_max=(curr_max+b)%l

        if curr_max==a:
            break
    
    print(mx)
