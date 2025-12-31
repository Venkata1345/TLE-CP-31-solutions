for _ in range(int(input())):
    n=int(input())
    s=''
    a=list(input().split())
    for i in a:
        if s=='':
            s=i 
        elif s+i < i+s:
            s=s+i 
        else:
            s=i+s 
    print(s)
