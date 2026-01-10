for _ in range(int(input())):
    n=int(input())
    l=list(range(n,0,-1))
    r=[n]+list(range(1,n))
    print(*(l+r))
