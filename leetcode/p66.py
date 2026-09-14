class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        lst=[]
        for i in digits:
            s+=str(i)
        s=int(s)+1
        s=str(s)
        for i in s:
            lst.append(int(i))
        return lst