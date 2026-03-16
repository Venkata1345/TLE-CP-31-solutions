n = int(input())
arr = list(map(int,input().split()))
max_watered =0
for i in range(n):
    curr_watered = 1
    for j in range(i-1,-1,-1):
        if arr[j]<=arr[j+1]:
            curr_watered+=1 
        else:
            break
    
    for j in range(i+1,n):
        if arr[j]<=arr[j-1]:
            curr_watered+=1
        else:
            break
    
    if curr_watered > max_watered:
        max_watered = curr_watered

print(max_watered)
