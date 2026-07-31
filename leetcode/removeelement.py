def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)-1
            
        for i in range(len(nums)):
            

            while j>=i and nums[j]==val:
                j-=1
            if i>j:
                break
            if nums[i]==val:
                
                nums[i]=nums[j]
                nums[j]=val
                j-=1
        return j+1
            