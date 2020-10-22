from collections import defaultdict

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # create a dictionary with a default value -1
        def default(): return -1
        cache = defaultdict(default)

        for i in range(1, amount+1):
            # base cases
            if i in coins:
                cache[i] = 1
                continue
            temp = []
            for c in coins:
                temp.append(cache[i - c])
            # unable cases
            if temp == [-1] * len(temp):
                cache[i] = -1
                continue
            else:
                temp = [v for v in temp if v != -1]
                cache[i] = min(temp) + 1
        return cache[amount]