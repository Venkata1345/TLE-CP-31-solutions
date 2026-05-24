for _ in range(int(input())):
    n, k = map(int, input().split())
    s= input()
    c=0
    left = -k-1
    for right in range(n):
        if s[right]=="1":
            if right-left>=k:
                c+=1
            left = right
    print(c)
