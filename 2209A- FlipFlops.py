for _ in range(int(input())):
    n, c , k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i]<=c:
            throws = min(k , c - a[i])

            k-=throws

            c= c+a[i]+throws
        else:
            break
    print(c)
