#check if a string is a palindrome
def check():
    n=input()
    l=0
    r=len(n)-1
    while l<r:
        if n[l]!=n[r]:

            return False
        l+=1
        r-=1
    return True

a=int(input())
for i in range(a):
   print(check())