for _ in range(int(input())):
    n=int(input())
    ans=[]
    for i in range(n):
        if i%2==0:
            ans.append(-1)
        else:
            ans.append(3)
    
    if n%2==0:
        ans[-1]=2 
    print(*ans)
