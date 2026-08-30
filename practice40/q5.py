# check if a number is prime 
def check_for_prime(a):
    import math
    if n<2:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0 :
        return False

    limit=int(math.sqrt(n))+1

    for i in range(5,limit,6):
        if n%i==0 or n%(i+2)==0:
            return False
        return True

n=int(input())
for _ in range(n):
    a=input()
    print(check_for_prime(a))