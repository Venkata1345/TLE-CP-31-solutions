for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = max(arr)*n
    print(ans)
