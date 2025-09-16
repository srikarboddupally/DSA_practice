def TopDownPath(grid) -> int:
    M, N = len(grid), len(grid[0])
    if grid[0][0]==1 or grid[M-1][N-1]==1:
        return 0
    cache = {(M-1, N-1):1}
    def dfs(r, c):
        if r==M or c==N:
            return 0
        if (r,c) in cache:
            return cache[(r,c)]
        #if (dp[r][c]!=-1): return dp[r][c]
        cache[(r,c)]= dfs(r+1,c)+ dfs(r,c+1)
        return cache[(r,c)]
    return dfs(0,0)

def BottomUpPath(grid) -> int:
    M, N = len(grid), len(grid[0])
    if grid[0][0]==1 or grid[M-1][N-1]==1:
        return 0
    dp = [[0]*((N+1) for _ in range(M+1))]
    dp[M-1][N-1]=1
    for r in reversed(range(M)):
        for c in reversed(range(N)):
            if grid[r][c]:
                dp[r][c]=0
            else:
                dp[r][c]+= dp[r+1][c]
                dp[r][c]+= dp[r][c+1]
    return dp[0][0]

def dpPath(grid)-> int:
    M, N = len(grid), len(grid[0])
    dp = [0]*(N+1)
    dp[N-1]=1
    for r in reversed(range(M)):
        for c in reversed(range(N)):
            if grid[r][c]:
                dp[c]=0
            else:
                dp[c]+=dp[c+1]
    return dp[0]


print(dpPath([[0,0,0],[0,1,0],[0,0,0]]))