''' search x no. in 1,4,9,16,25,36,49,64,81,100'''

nums = (1,4,9,16,25,36,49,64,81,100)

n = int(input("what is your no. : "))

i = 0
while i < len(nums):
    if(nums[i] == n):
        print("Found at index" , i)
        break;
    else :
        print("Not found")
    i+=1;
