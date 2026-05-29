def isprimeornot(n):
   if n<=1 :
    print("not prime")
    return
   for a in range (2,n):
     if n%a==0:
       print("not prime")
       return
     
   print("prime")

num1=int(input("n="))
isprimeornot(num1)

