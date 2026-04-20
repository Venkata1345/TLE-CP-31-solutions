for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = max(a)
    p = a.count(mx)
    print(p)
