def robMemo( nums: list[int]) -> int:
    cache = [-1]*len(nums)
    def dfs(i):
        if i>=len(nums): return 0
        if cache[i]!=-1:
            return cache[i]
        cache[i]= max(nums[i]+dfs(i+2), dfs(i+1))
        return cache[i]
    return dfs(0)

def robDP( nums: list[int]) -> int:
    rob1, rob2 =0, 0
    for num in nums:
        temp = max(num+rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(f"Maximum amount of money you can rob without alerting the police: {robDP([1,1,3,3])}")
