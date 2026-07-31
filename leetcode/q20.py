s="[]]"
# 
stack=[]

for i in s:
    if i in "({[" :
        stack.append(i)
        
    elif i==")" and stack and stack[-1]=="(":
        stack.pop()
        
    elif  i=="}" and stack and  stack[-1]=="{":
        stack.pop()
       
    elif  i=="]" and stack and stack[-1]=="[":
        stack.pop()
        
    else:
        print("false")
        break
else:
    if not stack:
        print("true")
    else:
        print("false")