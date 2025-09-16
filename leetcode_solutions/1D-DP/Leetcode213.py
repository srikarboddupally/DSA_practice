#Optimized 
def rob(nums: list[int]) -> int:
        return max(nums[0], helper(nums[1:]),helper(nums[:-1]))

def helper(nums):
    rob1, rob2 = 0, 0
    rob1, rob2 = 0, 0
    for num in nums:
        temp = max(num+rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
        
print(rob([2,9,8,3,6]))