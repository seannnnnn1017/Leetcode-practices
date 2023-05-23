s='   1 2 3'
cunt=0
for i in s:
    if i==' ':
        cunt+=1
    else:
        s=s[cunt::]
        break

print(s)