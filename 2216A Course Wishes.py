for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    courses = [(b[i], i+1) for i in range(n)]
    courses.sort(reverse= True)
    ops = []
    for level, course_id in courses:
        moves = (k+1) - level
        ops.extend([str(course_id)]* moves)
    
    print(len(ops))
    if ops:
        print(" ".join(ops))
    else:
        print()
