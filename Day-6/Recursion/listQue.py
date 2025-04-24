# W.A.P to print all the element in the list using recursive function

cities = ["Raipur","Jaipur","Udaipur","Jodhpur","Bikaner"]

def print_list(list , index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list , index+1)
    
print_list(cities)