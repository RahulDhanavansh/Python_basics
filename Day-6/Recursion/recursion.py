# Recursion = when a function call itself repeatedly


def show(n):  # n is a number
  if(n==0):   # if value of n is equal to 0 
     #(n==0) >= Base Case where loop has to stop
     return   # then exit or return
  print (n)   # if not then print n
  show(n-1)   # do n-1 until the value equals t0 0

  '''
  show(n=5) print 5

  show(n-1) = 5-1 =4 then print 4
  repeat until the value of n is equal to 0
  '''

show(5) #call function