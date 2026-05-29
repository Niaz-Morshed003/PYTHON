n=int(input("n="))
for a in range (1,n+1):
    if a==1:
        for b in range (1,n+1):
            print("Z",end="")
           
            
    elif a==n :
        for c in range (1,n+1):
            print("Z",end="")
            
    else:
        for d in range (a,n) :
            
            print(" ",end="")
        print("Z",end="")  
    print()      
