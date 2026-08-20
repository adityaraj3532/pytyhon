# for i in range (1,5):
#     print("*" *i)

n = 5  
i = 0
j = 0
for i in range(1, n + 1):
  for j in range(1, i + 1):
    print("*", end=" ")
  print()