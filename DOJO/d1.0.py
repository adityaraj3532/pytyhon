s = input()
ch = input()

sh = str(s)
i = 0 
l = len(s)
j = 0


for i in range (l):
    if sh[i] == ch:
        j+=1

print(j)        