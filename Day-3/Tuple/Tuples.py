print("Tuples")

# Tuples are immutable just like strings

tuple = (2,1,3,1)
print(tuple[0])

#tup[0] = 5
#we can not make changes in tuples just like list

tup = ();
print(tup)
#we can also create empty tuple

tupp = (1,)
print(tupp)
print(type(tupp))
# value treated as tuple
#this is the best way to create single value tuple

#what if we remove comma 
tuppp = (1)
print(tuppp)
print(type(tuppp))
# then value treated as integer