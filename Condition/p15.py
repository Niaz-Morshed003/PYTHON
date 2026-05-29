n=3
pl2=float(input("pl2="))
pl1=float(input("pl1="))
if pl1==pl2 and n!=0 : print("player 1 wins.")
elif n==0 : print ("player 2 wins")
else : 
    n=n-1
    print("chances left= ",n)
    pl1=float(input("pl1="))
    
    if pl1==pl2 and n!=0 : print("player 1 wins.")
    elif n==0 : print ("player 2 wins")
    else : 
          n=n-1
          print("chances left= ",n)
          pl1=float(input("pl1="))
          
          if pl1==pl2 and n!=0 : print("player 1 wins.")
          elif n==0 : print ("player 2 wins")
          else : 
            n=n-1
            print("chances left= ",n)
            pl1=float(input("pl1="))
            
            if pl1==pl2 and n!=0 : print("player 1 wins.")
            elif n==0 : print ("player 2 wins")
            else : 
             n=n-1
