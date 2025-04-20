#W.A.P to check if a list contain a palindrome of elements(Hint": use copy method )

# PALINDROME = words or a thing that are equal from both forward and backward

list = [1,2,3,2,1];

copy_list1 = list.copy();
copy_list1.reverse()

if(copy_list1 == list) :
    print("Palindrome")
else :
    print("Not Palindrome")

