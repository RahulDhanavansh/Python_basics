'''Loops are used for sequential traversal
for traversing list,string,tuples etc.
'''

#syntax
'''
for element in list :
    #some work


 for loop with else

    for element in list :
    #some work
else :
   # work when loop ends

'''

nums = [1,2,3,4,5,6,7,8,9]

'''for val in nums :
    print(val)


tuple = (12,21,2,12,3,4,5,54)

for x in tuple :
     print(x)'''


str = "Rahul Dhanavansh"

for char in str :
    if(char=='D'):
        print("Found")
        break;
    print(char)
else :("Not found")