n,a = map(int, input().split())
arr = list(map(int, input().split()))
c=0
a=a-1
for i in range(n):
    c+=arr[i]

i = a-1
j = a+1
while i>=0 and j<n:
    if arr[i]+arr[j]==1:
        c-=1 
    i-=1 
    j+=1 
print(c)
