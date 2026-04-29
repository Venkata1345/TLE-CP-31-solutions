for _ in range(int(input())):
    n = int(input())
    ans = []
    for k in range(1,18):
        divisor = (10 ** k)+1
        if n%divisor==0:
            ans.append(n//divisor)
    if not ans:
        print('0')
    else:
        ans.sort()
        print(len(ans))
        print(*ans)
