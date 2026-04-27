for _ in range(int(input())):
    n,m = map(int, input().split())
    p=0
    curr_time=0
    curr_side = 0
    for _ in range(n):
        req_time, req_side = map(int, input().split())
        dt = req_time - curr_time
        side= (curr_side+dt)%2
        if side == req_side:
            p+=dt
        else:
            p+=dt-1
        curr_time = req_time
        curr_side = req_side
    p = p + (m - curr_time)
    print(p)
