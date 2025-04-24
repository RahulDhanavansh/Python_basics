'''1,4,9,16,25,36,49,64,81,100'''

nums = [1,4,9,16,25,36,49,64,81,100]

'''for val in nums :
    print(val)'''


'''1,4,9,16,25,36,49,64,81,100'''

tup = [1,4,9,16,25,36,49,64,81,100]
#searching number x in tuple

n = int(input("the number is : "))
idx = 0;

for x in tup :
    if(x==n):
        print("no. is found at index :", idx , "no. is", x )
        break;
    idx+=1
else :
    print("Not found")