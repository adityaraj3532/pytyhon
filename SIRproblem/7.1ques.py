s = str(input())
l = int(len(s))
k = l
c = False

for i in range (0, int(l//2)):
    for j in range(l-1,(l//2)+1):
        if s[i] == s[j]:
            # print("ok")
            c = True
        else:
            # print("not ok")
            c= False
if c:
    print("ok")
else:
    aditya rajh ha nam mera
    
    print("not ok")


