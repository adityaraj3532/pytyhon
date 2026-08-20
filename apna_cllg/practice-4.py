#take two integer a and b as input.
#find and print thefirst number between 1 to 1000 that is divisible by both number

a = int(input(" "))
b = int(input(""))


for i in range(1, 1000):
    if (i % a == 0):
        if (i % b == 0):
            print (i)
            break