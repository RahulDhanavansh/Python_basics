#Methods

info = {
    "name" : "Rahul",
    "subjects" :{
"phy" : 97,
"chem" : 98,
"math" : 95
    }
}

# 1. Dict_name.keys() = return all the values

#print(info.keys());
# we can also convert these keys into a key or a tuple by using type casting
#print(list(info.keys()))

# 2. Dict_name.value() = return all the values
'''print(info.values())'''
# we can also convert these values into a key or a tuple by using type casting
#print(list(info.value()))
'''
print(list(info.values()))
print(len(list(info.values())))'''

# 3.  Dict_name.items() = returns all key value pairs as tuple
#print(info.items());
# we can also type cast to it into alist
'''pairs = list(info.items())
print(pairs[0])
print(pairs[1])
'''


# 4. Dict_name.get("key") #return the key according to value
#print(info.get("name"))

#we can simply fetch the value of key then why we need the get method
'''
print(info["name"])
print(info.get("name))

Both statement give same outout then why we need get method
so if we write wrong key then

print(info["name"]) returns error
print(info.get("name)) returns None


#Note :-
print(info["name"]) returns error
after this statement if we write right lines of codes then they will not execute

print(info["name2"]) 
print("namefda") 
print("namdafe") 
print("naafme")
print("namgfe")  '''


# 5. Dict_name.update() to update the dictionary
info.update({"city" : "jaipur"})
print(info)

# we can also put it into new dictionary
new_dict = {
    "name" : "Rahul Dhanavansh",
" city" : "jaipur",
"age" : 56,
}

info.update(new_dict)
print(info)