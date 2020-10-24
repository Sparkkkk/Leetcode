class Solution:

    # f(nums, S) = sum(f(nums \ ni, S +/- ni ))
    # f([1,1,1,1], 2) = 4 = f([1,1,1], 2+1) + f([1,1,1], 2-1)

    # f([1,1,1,1], 4) = 1
    # f([1,1,1], 4+1) = 0
    # f([1,1,1], 4-1) = 1
    # f([1,1,1,1,1], 3) = f([1,1,1,1], 3 - 1) + f([1,1,1,1], 3 + 1) = 4 + 1 = 5
    # state represent by (index, target)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        cache = {}

        def helper(index, target):
            if index == len(nums):
                if target == S:
                    return 1
                else:
                    return 0
            if (index, target) not in cache.keys():
                cache[(index, target)] = helper(index + 1, target + nums[index]) + helper(index + 1,
                                                                                          target - nums[index])

            return cache[(index, target)]

        return helper(0, 0)