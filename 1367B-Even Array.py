for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    c_odd=0
    c_eve=0
    req_even=(n+1)//2
    req_odd=n//2
    for i in range(n):
        if arr[i]%2==0:
            c_eve+=1 

    if c_eve!=req_even:
        print(-1)
        continue
        
    misplaced_c=0
    for j in range(n):
        if j%2==0:
            if arr[j]%2!=0:
                misplaced_c+=1 
    
    print(misplaced_c)
