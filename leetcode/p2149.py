class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        sign=[0]*len(nums)
        neg=1
        pos=0
        for i in nums:
            if i >0:
                sign[pos]=i
                pos+=2
                
            elif i<0:
                sign[neg]=i
                neg+=2
               
        return sign