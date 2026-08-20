s = input()

vowel_count = 0
vowels = "aeiouAEIOU"

for char in s:
    if char in vowels:
        vowel_count+=1
        print(f"{char}", end = (" "))

