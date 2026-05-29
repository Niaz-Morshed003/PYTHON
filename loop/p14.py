n=int(input("n="))
r=int(input("r="))
z=n-r
result1=1
result2=1
result3=1
for i in range (1,n+1):
    result1=i * result1
for a in range (1,r+1)  :
    result2=a * result2  
for b in range (1,z+1):
    result3=b * result3
print("ncr=",result1/(result2 * result3))    