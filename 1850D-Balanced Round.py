for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    max_seq=1
    c=1
    a.sort()
    for i in range(n-1):
        if abs(a[i]-a[i+1])<=k:
            c+=1
        else:
            c=1
        max_seq=max(max_seq,c)      
    print(n-max_seq)
