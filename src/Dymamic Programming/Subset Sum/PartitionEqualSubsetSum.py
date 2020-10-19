# Subset Sum Problem
# Base case
# Q(0,T) = nums[0] == T
# Recursive case
# Q(N,T) = Q(N-1,T) or Q(N-1, T-nums(N)) or nums[n] == target
# Then solve it by using Memorization
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        nums.sort()
        cache = dict()

        def helper(index, target):
            if index == 0:
                cache[(index, target)] = nums[index] == target
                return cache[(index, target)]
            if (index, target) in cache:
                return cache[(index, target)]
            cache[(index, target)] = helper(index - 1, target) or nums[index] == target or helper(index - 1, target - nums[index])
            return cache[(index, target)]
        
        return helper(len(nums) - 1, sum(nums) // 2)