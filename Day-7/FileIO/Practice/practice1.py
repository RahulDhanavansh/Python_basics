# W.A.P to create a new file using python and add following data in it

'''
Hi everyone
we are learing File I/O
using Java
'''

file = open("E:\Python by AC\Day-7\FileIO\Practice\practice.txt", "w")

data = file.write("Hi everyone \n we are learning File I/O \n using java")

print(data);

file.close()