for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cz=a.count(0)
    l=0
    while l<n and a[l]==0:
        l+=1
    r=n-1
    while r>=0 and a[r]==0:
        r-=1
    
    found=False
    for i in range(l,r+1):
        if a[i]==0:
            found=True
            break
    
    if cz==n:
        print('0')
    elif not found:
        print('1')
    else:
        print('2')
    
