selection = input()
money = int(input())
price = 25
if money >= price:
    change = money - price
    print("you have purchecased", selection)
    print("Your change is:", change)