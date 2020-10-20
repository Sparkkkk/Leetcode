class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        # search space - for each matchstick there are 4 possbilities
        # base case 
        # if len(path) == n
        # check if result are equal
        # otherwise try each possiblities and then backtrack
        if nums == None or len(nums) < 4:
            return False
        
        target = sum(nums) // 4
        if target * 4 != sum(nums):
            return False
        
        nums.sort(reverse=True)
        results = [0 for _ in range(4)]
        
        def backtrack(index):
            if index == len(nums):
                return results[0] == results[1] == results[2] == target
            else:
                for i in range(4):
                    results[i] += nums[index]
                    # pruning
                    if results[i] > target:
                        results[i] -= nums[index]
                        continue
                    
                    # go to next level
                    res = backtrack(index + 1)
                    # check the result of one subtree if we can find one valid answer
                    if res:
                        return True
                    # revert state back to previous level
                    results[i] -= nums[index]
                return False
        return backtrack(0)