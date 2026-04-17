for _ in range(int(input())):
    n = int(input())
    s = input()
    c=2
    for i in range(n-1):
        if s[i]==s[i+1]:
            c+=1
        else:
            break
    print(c)
