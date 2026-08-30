#check if a number is a palendrom
try:
    n=int(input())
except(EOFError,ValueError):
    print("only number allowed")
try:
    if n<0:
        print("number is not palendrome")
except(NameError):
    print("number only")
else:
    ln=list(str(n))
    left=0
    right=len(str(n))-1
    ispalindrome=True
    while left<right:
        if ln[left] != ln[right]:
            ispalindrome=False
            break
        left+=1
        right-=1
    print(ispalindrome)