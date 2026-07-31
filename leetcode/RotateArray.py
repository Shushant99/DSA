def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0,nums.pop())



#2

def rotate(self, nums: List[int], k: int) -> None:
        k%=len(nums)
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        