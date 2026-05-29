file=open("file1","w")
file.write("LOSER\n")
file.write("ZERO\n")
file.write("Failure\n")
file.close()
file=open("file1","r")
content=file.read()
file.close()
file=open("file1","r")
count=0
for line in file:
    count=count+1
file.close()
file=open("file2","w")
file.write("The line numbers from previous file- ")
file.write(str(count))
file.write("\nContents from the previous file-\n")
file.write(content)
file.close()
file=open("file1","a")
file.write("\nBounce back\n")
file.write("Resilance\n")
file.write("Fulfillment")
file.close()
file=open("file1","r")
content1=file.read()
file.close()
file=open("file1","r")
count1=0
for line in file:
    count1=count1+1
file.close()
file=open("file2","a")
file.write("\n")
file.write("line in file 1- ")
file.write(str(count1))
file.write("\n")
file.write("Contents from file 1-\n")
file.write(content1)
file.close()



