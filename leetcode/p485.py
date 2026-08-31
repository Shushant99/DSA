class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        cons=0
        temp=0
        for i in nums:
            if i ==1:
                temp+=1
            elif i!=1:
                temp=0
            if temp>cons:
                cons=temp
            
        return cons