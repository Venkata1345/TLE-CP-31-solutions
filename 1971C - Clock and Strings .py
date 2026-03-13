for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    if a > b :
        a,b = b,a 
    c_in = a<c<b
    d_in = a<d<b

    if c_in!=d_in :
        print("YES")
    else:
        print('NO')
