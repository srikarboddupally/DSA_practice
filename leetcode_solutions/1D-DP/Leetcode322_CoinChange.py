from collections import deque
class Solution:
    def coinChangeBFS(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1
    
    def memo(self, coins, amount) -> int:
        if amount==0:
            return 0
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            res = 1e9
            for coin in coins:
                if i-coin >=0:
                    res = min(res, dfs(i-coin)+1)
            cache[i]=res
            return res
        minCoins = dfs(amount)
        return -1 if minCoins>=1e9 else minCoins
        # TC : 0(N*M)
        # SC : 0(M)

    def tabulationFindMinCoins(self, coins, amount)-> int:
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for amt in range(1, amount+1):
            for coin in coins:
                if amt-coin >=0:
                    dp[amt]= min(dp[amt],1+dp[amt-coin])

        return -1 if dp[amount]==amount+1 else dp[amount]
    # TC : 0(N*M)
    # SC : 0(M)




sol = Solution()
print(sol.coinChangeBFS([1,5,10],12))
print(sol.tabulationFindMinCoins([1,5,10],12))
# TC : 0(N*M)
# SC : 0(M)

