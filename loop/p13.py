digit = int (input("digit="))
result = 1

for i in range (1,digit+1):
    result=i*result
print("factorial of digit =",result)