s=input()
up=0
low=0
for char in s:
    if 'A'<=char<='Z':
        up+=1
low=len(s)-up
if up>low:
    print(s.upper())
else:
    print(s.lower())
