for _ in range(int(input())):
    s=input()
    row=s[0]
    column=s[1]
    for i in 'abcdefgh':
        if i!=row:
            print(i+column)
    for j in '12345678':
        if j!=column:
            print(row+j)
