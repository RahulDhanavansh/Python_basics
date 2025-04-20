#Dictionary are used to store data values in key:value pairs. They are unordered, mutable and don't allow duplicate keys

# we can also add and create list and tupples in dictionary


myInfo = {

    #"key" = "value"
    "name" : "Rahul",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dictionary", "set"),
    "age" : 22,
    "learning" : "coding",
}

print(myInfo);
print(type(myInfo))

#to fetch or access value

print(myInfo["name"])
print(myInfo["subjects"])
print(myInfo["age"])
print(myInfo["learning"])

#to assign new values in dictionary

myInfo["name"] = "Rahul Dhanavansh";# pyhton overwrite the values
myInfo["college"] = "Poddar"
print(myInfo)

# Null dictionary
nullDict = {}
nullDict["name"] = "ME"
print(nullDict)