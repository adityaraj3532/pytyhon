n = int(input())
b = input().split()

x = 0 

for op in b:
    if '+' in op:
        x+=1        cq
    else:
        x-=1

print(x)