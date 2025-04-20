
#1. 
# '''Store following word meanings in a python dictionary : table : "a piece of furniture", "list a fact of figures"cat : " a small animal" '''

new_Dict = {
    "table" : ["a piece of furniture" ,"list a fact of figures"],
    "cat" : "a small animal",
}

print(new_Dict)

# 2.
'''
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.

”python”,“java”,“C++”,“python”,“javascript”,“java”“python“java”,“C++”,“C"
'''

classrooms = {
    "python","java","C++","python","javascript","java","python","java","C++","C" }

print(len(classrooms))

'''
#3.
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.

'''

'''marks = {}
print(type(marks))

x = (int(input("Enter the value of first subject : ")))
marks.update({"physics" : x})

y = (int(input("Enter the value of second subject : ")))
marks.update({"chemistry" : y})

z = (int(input("Enter the value of third subject : ")))
marks.update({"maths" : z})

print(marks)'''

"""
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)
"""

set = {("float" , 9.0),("int" , 9)}
set = {9 , "9.0"}
print(set)