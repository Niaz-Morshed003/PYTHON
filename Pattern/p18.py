n=int(input("n="))
for a in range (1,n+1):
    if a==((n//2)+1):
        for b in range (1,n+1+1):
            print("H",end="")
        print() 
    else:
        print("H",end="") 
        for c in range (1,n)  :
            print(" ",end="")  
        print("H",end="") 
        print()     