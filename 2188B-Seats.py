for _ in range(int(input())):
    n = int(input())
    s = input()
    c=0
    blocks = s.split('1')
    if len(blocks) == 1:
        l = len(blocks[0])
        c+= (l+2)//3
    else:
        # left edge
        c += (len(blocks[0]) + 1 )//3
        # right edge
        c += (len(blocks[-1])+1)//3
        for i in range(1, len(blocks)-1):
            c+=len(blocks[i])//3
    prev = s.count('1')
    total = prev + c
    print(total)
