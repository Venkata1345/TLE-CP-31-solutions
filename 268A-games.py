n=int(input())
home=[]
guest=[]
for _ in range(n):
    h,g=map(int,input().split())
    home.append(h)
    guest.append(g)

c=0 
for i in range(n):
    for j in range(n):
        if home[i]==guest[j]:
            c+=1 
print(c)
