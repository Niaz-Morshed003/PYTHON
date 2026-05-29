a=float(input("a="))
b=float(input("b="))
opt=int(input("opt="))
if opt==1:print("a+b",a+b)
elif opt==2:print("a-b",a-b)
elif opt==3:print("a*b",a*b)
elif opt==4:
    if b==0:print("invalid")
    else:
        case=int(input("case="))
        if case==1:print("a/b",a/b)
        elif case==2 : print("a/b",a%b)
        else:print("invalid")

else:print("invalid")