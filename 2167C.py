for _ in range(int(input())):
    n=int(input())
    toys=list(map(int,input().split()))
    p=toys[0]%2
    for i in toys:
        if i%2!=p:
            print(*sorted(toys))
            break
    else:
        print(*toys)
