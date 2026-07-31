nums=[3,2,3]
dicto={}
for i in nums:
    if i not in dicto.keys():
       dicto[i] = 1
    else:
         dicto[i] += 1
    if dicto[i]>(len(nums)//2):
        print(i)