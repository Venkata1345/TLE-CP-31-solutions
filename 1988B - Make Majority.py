for _ in range(int(input())):
    n = int(input())
    s = input()
    one_c =0 
    zero_block = 0
    for i in range(n):
        if s[i] == '1':
            one_c+=1 
        elif s[i]=='0':
            if i==0 or s[i-1]=='1':
                zero_block+=1 
    
    if one_c > zero_block:
        print("YES")
    else:
        print('NO')
