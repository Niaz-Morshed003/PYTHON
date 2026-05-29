Biodata={
    "Name": "Niaz Morshed",
    "Age":23,
    "University":"United International University",
    "Cgpa": 1.78,
    "Courses":["Economics","DSA 2 theory","Statistics","Calculus"],
    "Grades":("A-","B-","C-","D-"),
    #dictionary is also mutable
    #"key": 899
    1.89:"ok",
    1:5,
    #[3.5,7.8,6,5,4]:78, list mutable so can not be key
    (66,"ok",):"ko"
    #dic hocche like kono order nai. Ekta key ekbar e thakee

}
print(Biodata)
print(type(Biodata))
#accessing individually:
print(Biodata["Grades"])
print(Biodata[1.89])
#baire theke change and add:
Biodata["Name"]="Morshed"
Biodata["Surname"]="Howlader"
print(Biodata)
Nulldict={}
print(Nulldict)
Nulldict["Name"]="R"
print(Nulldict)
#Nested dictionary:
Nesteddict={
    "Name":"Messi",
    "Attributes":{
        "Dribbling":100,
        "Scoring":95,
        "Assisting":100,
        "Diving":00

    }
}
print(Nesteddict)
print(Nesteddict["Attributes"])
print((Nesteddict)["Attributes"]["Diving"])

#Method:

print(Biodata.keys())
print(Nulldict.keys())
print(Nesteddict.keys())
#nested dic e je arekta dic ache shetar keys print hobee na .
print(len(Biodata))
print(len(Nulldict))
print(len(Nesteddict))
print(Biodata.values())
#typecasting the values to the lsit
print(list(Biodata.values()))
#ekhon etar length ber kori cholo
print(len(list(Biodata.values())))
print(Biodata.items())#print korbee as tuple
#next 2 line er kaaj shesh
print(Biodata["Grades"])
print(Biodata.get("Grades"))
#key oi dictionary te ache ki na bujhar jonno:
print(Biodata.get("Sij"))#none ashbe
Biodata.update({"City":"Dhaka"})
print(Biodata)
Newdict={"PS":"Badda"}
Biodata.update(Newdict)
print(Biodata)
print(Biodata.update({"Name":"Goslin"}))
print(Biodata)
#SET
#Set er o kono order nai,same jinish duibar store kora jabee na and eta immutable
#dict and list, set er moddhe store kora jabee na karon tara mutable,but string and tuole jabee karon tara immutable
Set1={1,4.4,"DDD",("a",6,5.7),1}
print(Set1) #duplicate item print korbee na
print(type(Set1))
print(len(Set1)) #duplicate baad diye length count korbe
Emptyset=set()
print(Emptyset)
print(len(Emptyset))
#set is mutable but set er bhitor thaka element immutable
Emptyset.add(1)
Emptyset.add(("a","str"))#ekbaree just ekta element ney.
print(Emptyset)
Emptyset.remove(1)
print(Emptyset)
Set1.clear()
print(Set1)
Set2={"Strrr",44,44.55,("sss",999,23,55,66)}
print(Set2)
print(Set2.pop())#random jekono element pop hobee
Set3={"Strrr",44,44.55,("sss",999,23,55,66),69}
print(Set2.union(Set3))
print(Set2.intersection(Set3))
#Question1:Store following word meanings in a python dictionary :
#table : "a piece of furniture", "list of facts & figures"
#cat : "a small animal"
WordMeaning={
    "Cat":"A small animal",
    "Table":["A piece of Furniture","List of facts and figures"]
}
print(WordMeaning)
# Question 2:
# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"
Students={"python", "java", "c++", "python", "javascript","java", "python", "java", "c++", "C"}
print(len(Students))
# Question 3:
# WAP to enter marks of 3 subjects from the user
# and store them in a dict. Start with an empty dictionary & add one by one.
# Use subject name as key & marks as value.
Sub={}
Phy=int(input("Phy="))
Chem=int(input("Chem="))
Bio=int(input("Bio="))
Sub.update({"Phy":Phy})
Sub.update({"Chem":Chem})
Sub.update({"Bio":Bio})
print(Sub)
# Question 4:
# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
Sset={9,9.0}
print(Sset)#just 9 print hobee
SSet={"9",9.0}
print(SSet)
#another way:
Way={("Flaot",9.0),("Int",9)}
print(Way)