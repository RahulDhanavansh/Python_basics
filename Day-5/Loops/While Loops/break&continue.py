''' Break and Continue'''

# Break is used to terminate the loop when encountered
'''i = 1
while i <=10 :
    print(i)
    if(i==7):
        break
    i+=1

print("Ending")'''


# Continue terminate execution in the current iteration & continues execution of the loop with the next iteration

i = 1
while i <=10 :
    if(i==7):
        i+=1
        continue
    print(i)
    i+=1