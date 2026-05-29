file=open("Niaz's file","r")
count=0
for line in file:
    count=count+1
print("line-",count)    
file.close()