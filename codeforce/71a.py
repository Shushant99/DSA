def solve():
    n=input()
    if len(n)<=10    :
        return n
    else:
        return n[0]+str(len(n)-2)+n[len(n)-1]

i=int(input())
for _ in range(i):
    print(solve())