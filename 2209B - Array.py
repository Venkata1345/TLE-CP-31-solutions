for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        smaller_count =0
        larger_count =0
        for j in range(i+1,n):
            if a[j]>a[i]:
                larger_count+=1 
            if a[j] < a[i]:
                smaller_count+=1
        ans.append(str(max(smaller_count, larger_count)))
    print(' '.join(ans))
