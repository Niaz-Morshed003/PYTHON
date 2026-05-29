List=[44.5,45.6,89.9,56.78,67.89]
print(List)
print(type(List))
print(List[3])
print(List[4])
print(len(List))
List1=["NIAZ","BADDA",88,88.67]
print(List1)
#in python,string is unchangable
#in python,list is changable
str="niaz"
print(str[0])
#str[0]=y-not allowed in py
List1[1]="Raiyan"
print(List1)
#now list slicing:
List2=[88,44,55,66,22,11,444]
print(List2[2:5])
print(List2[:5])
print(List2[0:])
List2.append(78)
#mutation or change korlam
print(List2)
List2.sort()
print(List2)
List2.sort(reverse=True)
print(List2)
List3=["opple","inter","bgfngng" "vanilla","awer"]
List3.sort()
print(List3)
List3.sort(reverse=True)
print(List3)
List3.reverse()
print(List3)
List4=[322,445,889,345,453]
List4.insert(2,999)
print(List4)
List4.remove(322)
print(List4)
List4.pop(1)
print(List4)
#Now tuples: change kora jay na,immutable
Tup1=(99.6,55,34.5,22,"NIAZ")
print(Tup1)
print(type(Tup1))
print(Tup1[3])
EmptyTup=()
print(EmptyTup)
SinglevalueTup=(2,)
print(SinglevalueTup)
#SinglevalueTup=(2) ke integer hishebe treat korbe
#Tuple er slicing same as List
Tup2=(55,78.99,45.77,22,33,44)
print(Tup2.index(22))
print(Tup2.count(55))
#wap to store your 3 fav movies in a list taking inpput
mov1=input("name:")
mov2=input("name:")
mov3=input("name:")
movlist=[mov1,mov2,mov3]
print(movlist)
#WAP to check whether the list contains a palindrome of elements or not
llist=[3,6,3]
lllist=llist.copy()
lllist.reverse()
if llist==lllist:
    print("Palindrome")
else:
    print("Not a palindrome")

#write a program where amount of A grade will be counted in a Tuple
tupp1=("A","E","C","B","D","A")
print(tupp1.count("A"))
#store the above tupple in a list and sort them
lList=["A","E","C","B","D","A"]
lList.sort()
print(lList)