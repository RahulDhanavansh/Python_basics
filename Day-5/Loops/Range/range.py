'''
Range is a function that return a sequence of numbers, start from 0 by default and increment by 1(by default),and stop before specific number

syntax
range(start?, stop, step?)
'''
#sequence = range(5)

for i in range(10) :
    print(i)

#start(option by default 0)
#stop(neccessary)
#step(by default 1)
#step = how much you want to increase

for i in range(10) : #range(stop)
    print(i)

for i in range(2,10) :#range(start stop)
     print(i)

for i in range(2,10,1) :#range(start stop step)
    print(i)
    #output = 2,4,6,8