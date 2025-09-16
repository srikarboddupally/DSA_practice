def climbingStairsMemo(n, cache):
    cache = [-1]*n
    def dfs(i):
        if i>=n: return i==n
        if cache[i]!=-1:
            return cache[i]
        cache[i]= dfs(i+1,cache)+dfs(i+2,cache)
        return cache[i]
    return dfs(0)

def climbingStairsDP(n): #Space-optimized
    one, two = 1, 1
    for i in range(2, n+1):
        one, two = two, one+two
    return two

# print(climbingStairsDP(5))