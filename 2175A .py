for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    unique = len(set(arr))
    while unique not in set(arr):
        unique+=1 
    print(unique)
