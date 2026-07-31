nums=[0,1,0,3,12]

pl = 0
pr = 0

while pr < len(nums):
    if nums[pr] != 0:
        nums[pl], nums[pr] = nums[pr], nums[pl]
        pl += 1
    pr += 1

print(nums)
