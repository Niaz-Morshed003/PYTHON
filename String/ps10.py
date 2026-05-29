text=input("String:")
reversed=""
for ch in text:
    reversed=ch+reversed
print("reversed:",reversed)    
if text==reversed:
    print("Yes,palindrome")
else:
    print("No,not a Plindrome")