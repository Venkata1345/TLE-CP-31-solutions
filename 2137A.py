for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    l = list(s)
    sleep = 0
    awake = 0
    for i in range(n):
        if s[i] == '1':
            awake = k
        else:
            if awake>0:
                awake-=1
            else:
                sleep+=1 
    print(sleep)
