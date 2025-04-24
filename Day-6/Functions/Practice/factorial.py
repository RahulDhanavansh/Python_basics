

n = int(input("Enter your number : "))

def calc_fact(n):
    fact = 1;
    for x in range(1 , n+1):
        fact*=x
    print(fact)

calc_fact(n)
