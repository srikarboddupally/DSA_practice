def minClimbing( cost: list[int]) -> int:
    cache = [-1]*len(cost)
    def dfs(i):
        if i>=len(cost): return 0
        if cache[i]!=-1:
            return cache[i]
        cache[i]= cost[i]+min(dfs(i+1), dfs(i+2))
        return cache[i]
    return min(dfs(0), dfs(1))

def minClimbingDP( cost: list[int]) -> int:
    n = len(cost)
    for i in range(n-3, -1,-1):
        cost[i]+= min(cost[i+1],cost[i+2])

    return min(cost[0], cost[1])

print(f"Minimum cost to reach the top of the floor: {minClimbingDP([1,2,1,2,1,1,1])}")