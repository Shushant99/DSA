class Solution:
    def maximumSubarraySum(nums, k):
        winsum=0
        for i in range(k):
            winsum+=nums[i]
            maxsum=winsum
            maxsum=max(winsum,maxsum)
        for i in range(k,len(nums)):
            winsum+=nums[i]
            winsum-=nums[(i-k)]
            maxsum=max(winsum,maxsum)
        return maxsum

b=Solution
nums=[1,5,4,2,9,20,15,7,6,3,50]
k=3
a=b.maximumSubarraySum(nums , k)
print(a)