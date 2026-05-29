answer=0
answer1=0
n=int(input("n="))
for i in range (1,n+1):
    answer=(answer*10)+i
    answer1=answer1+answer
print("result=",answer1)    