class Solution:
# BruteForce (o^2) not suggested
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j: 
                    sum = nums[i]+nums[j]
                if sum == target:
                    return [i, j]
    
    def twoSum