class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        sumS = sum(stones)
        for a in stones:
            dp |= {a + i for i in dp}
        return min(abs(sumS - i - i) for i in dp)