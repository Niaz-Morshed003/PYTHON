text=input("String:")
count=0
for ch in text:
    if ch in "aeiouAEIOU":
        count=count+1
print("Total vowel is :",count)        