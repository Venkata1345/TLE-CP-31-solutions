n,h = map(int, input().split())
arr = list(map(int,input().split()))
sm=0
for i in range(n):
    if arr[i]>h:
        sm+=2
    else:
        sm+=1
print(sm)
