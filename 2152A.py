for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = len(set(arr))
    print(2*k-1)
