#W.A.P to search "learning" word in practice.txt file


#newData = data.find("learning")
#print(newData)

#using functions
def check_the_word():
     word = "learning"
     with open("E:\Python by AC\Day-7\FileIO\Practice\practice.txt", "r") as file:
        data = file.read()
        if(data.find(word)!= -1):
            print("Found")
        else:
            print("Not found")

#check_the_word()


# for checking line 

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("E:\Python by AC\Day-7\FileIO\Practice\practice.txt", "r") as file:
        while data :
            data=file.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()