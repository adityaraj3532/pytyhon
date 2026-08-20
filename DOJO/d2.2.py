n = int(input())

for i in range (1,n+1):
    star = "* " * i 
    print (star)

j= n-1

while(j>0):
    st = "* " * j
    print(st)

    j-=1
