# Sets

'''
* Sets are collection of unordered items
* each and every item or element is unique and immutable

***
Sets are mutable but elements in set are immutable


nums = {1,2,4,5,2}
sets = {1,2,2,2}

repeated items are only stored once so it is resolved as {1,2}
'''
collection = {1,2,3,4 , "hello", "r" ,"r"}
print(collection)
print(type(collection))
print(len(collection)) #total numbers in set

#Empty Set
collection_1 = set()
print(collection_1)
print(type(collection_1))