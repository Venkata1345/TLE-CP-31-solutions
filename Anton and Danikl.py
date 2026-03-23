n = int(input())
s = input()
c_a,c_d = 0,0
for i in range(n):
    if s[i]=='A':
        c_a+=1
    else:
        c_d+=1
if c_a > c_d:
    print('Anton')
elif c_a < c_d:
    print('Danik')
else:
    print('Friendship')
