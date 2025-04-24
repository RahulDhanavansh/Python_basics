file = open("E:\Python by AC\Day-7\FileIO\demo.txt", "r")
data = file.read()
print(data)
print(type(data))
file.close()


'''
'r' = open for reading (default)
'w' = open for writing, truncating the file first
truncating = all data will delete first then you will able to write
'x' = create a new file and open it for writing
'a' = open for writing, append to the end of the file if it exist
'b' = binary mode
't' = text mode
'+' = open a disk file for updating(read and write)





'''
