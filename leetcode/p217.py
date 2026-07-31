class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in freq.values():
            if i !=1:
                return True
        else:
            return False
        

# or 

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset=set(nums)
        if len(nums)!=len(myset):
            return True
        else:
            return False

# or

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset=set(nums)
        return len(nums)!=len(myset)
            