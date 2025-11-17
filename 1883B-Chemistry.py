for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    char_count={}
    for i in s:
        if i in char_count:
            char_count[i]+=1
        else:
            char_count[i]=1
    odd_count=0
    for j,v in char_count.items():
        if v%2!=0:
            odd_count+=1

    if odd_count<=(k+1):
        print('YES')
    else:
        print('NO')
