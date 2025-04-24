# From a file conataining numbers sepreated by comma, print the count of even numbers
count = 0;
with open("E:\Python by AC\Day-7\FileIO\Practice\sample.txt", "r") as file:
        data = file.read()
print(data)

nums = data.split(",")
print(nums)
for val in nums:
        if(int(val)%2 == 0):
                count+=1

print(count)