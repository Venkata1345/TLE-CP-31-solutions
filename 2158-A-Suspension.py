for _ in range(int(input())):
    n=int(input())
    y,r=map(int,input().split())
    ans= y//2 + r
    print(min(ans,n))
