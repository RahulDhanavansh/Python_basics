file  = open("E:\Python by AC\Day-7\FileIO\demo.txt" , "r")

# data = file.read() => for reading file

#for reading particular data

line1 = file.readline()
#readline(5) = 5 for index (print value of starting 5 index in a string)
print(line1)

line2 = file.readline()
print(line2)

line3 = file.readline()
print(line3)

file.close()

'''
r+
:-  read + overwrite
:-  pointer at start
:-  no truncate
'''