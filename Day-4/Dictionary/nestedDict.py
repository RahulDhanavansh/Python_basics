# Nested Dictionary

student = {
    "name" : "Rahul",
    "subjects" :{
"phy" : 97,
"chem" : 98,
"math" : 95
    }
}

print(student)

# for single entity
print(student["subjects"])

#for more specific
print(student["subjects"]["chem"])