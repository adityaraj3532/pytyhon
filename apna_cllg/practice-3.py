#print all the multiple of 3 from 1 to 50 skip 15
for i in range(1 , 50):
    if(i == 15):
        continue
    if(i % 3 == 0):
        print(i)
