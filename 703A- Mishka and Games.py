n=int(input())
m,c=0,0
for i in range(n):
    mi,ci=map(int,input().split())
    if mi>ci:
        m+=1
    elif mi<ci:
        c+=1

    
if m>c:
    print('Mishka')
elif m<c:
    print('Chris')
else:
    print('Friendship is magic!^^')
