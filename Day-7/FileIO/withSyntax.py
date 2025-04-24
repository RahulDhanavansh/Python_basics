with open("E:\Python by AC\Day-7\FileIO\demo.txt" ,"r") as file:

    data = file.read()
    print(data)

    with open("E:\Python by AC\Day-7\FileIO\demo.txt" ,"w") as file:

     file.write("new data")
    
    with open("E:\Python by AC\Day-7\FileIO\demo.txt" ,"a") as file:

     file.write("\n what should i do now \n i dont know what to do \n i dont know what to do \n tauubaaaaa \n aage kya kru")
    