first_line = input().split()

n = int(first_line[0])
m = int(first_line[1])
c = first_line[2]

matrix= []
for _ in range(n):
    row = input()
    matrix.append(row)

deputies = set()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == c:
            # above
            if i>0:
                n1 = matrix[i-1][j]
                if n1!='.' and n1!=c:
                    deputies.add(n1)
            
            # below
            if i < n-1:
                n1 = matrix[i+1][j]
                if n1!='.' and n1!=c:
                    deputies.add(n1)
            
            # left
            if j > 0:
                n1 = matrix[i][j-1]
                if n1!='.' and n1!=c:
                    deputies.add(n1)
            #right
            if j < m-1 :
                n1 = matrix[i][j+1]
                if n1!='.' and n1!=c:
                    deputies.add(n1)

print(len(deputies))
