def generateprime(n):
    if n<=1:
        print("No prime numbers are there")
        return
    print("prime numbers are:",)
    print()
    for a in range (2,n):
        if a==2:
            print("prime-",a)
            continue
        for b in range (2,a):
            flag=0
            if a%b==0:
                print(" not prime-",a)
                flag=1
                break
        if flag==0:
            print("prime-",a)    
        
            
    return
   
num1=int(input("num1="))     
generateprime(num1)