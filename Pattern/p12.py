n=int(input("n="))
g=n//2
l=g+1
for a in range (0,l):
    for b in range(1,l-a):
        print(" ",end="")

    for c in range (0,(a*2)+1):
        print("x",end="")  
    print()    



for d in range (1,g):
    for e in range (0,d):
        print(" ",end="")
    for f in range (d,n-d)  :
        print("x",end="")  
    print()