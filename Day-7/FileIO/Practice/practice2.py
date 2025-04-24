#W.A.P to replaces all occurences of "java" with "python" in practice.txt file

file = open("E:\Python by AC\Day-7\FileIO\Practice\practice.txt" ,"r" )
data = file.read()

newData = data.replace("java" , "python")
print(newData)

with open("E:\Python by AC\Day-7\FileIO\Practice\practice.txt","w") as file:
 file.write(newData)