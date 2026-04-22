for _ in range(int(input())):
    n,a = map(int, input().split())
    v = list(map(int, input().split()))
    greater_than_a = 0
    lesser_than_a =0
    for i in range(n):
        if v[i]<a:
            lesser_than_a+=1
        if v[i]>a:
            greater_than_a+=1
    if lesser_than_a>greater_than_a:
        b = a-1
    else:
        b = a+1
    print(b)
