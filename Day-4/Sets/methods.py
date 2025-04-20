#Methods

collection = {1,2,3,4 , "hello"}

#1. set.add(element) to adds an element
collection.add("5")
collection.add(5)
collection.add("we")
collection.add((1,2,3))#we can add tuples but can not list

'''
***
if we try to add a list we get error

collection.add([1,2,3])
TypeError: unhashable type: 'list'

unhashable : specific algorithm which is used to convert original thing into something else
or immutable things
'''
print(collection)

#2. set.remove(element) to removes an element
collection.remove("5")
collection.remove(5)
print(collection)

#3. set.clear() to clear(empties) the set
collection.clear()
print(collection)


collection.add("5")
collection.add(5)
print(collection)

#2. set.pop() to removes a random value
collection.pop()
print(collection)



# IMPORTANT METHODS

# 1. set.union(set2) combines both set values and return new

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))


# 2. set.intersection(set2) combines common set values and return new

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.intersection(set2))

