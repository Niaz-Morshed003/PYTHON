Text=input("String:")
result=""
for ch in Text:
    if ch.islower():
        result=result+ch.upper()
    else:
        result=result+ch.lower()
print("After toggling:",result)