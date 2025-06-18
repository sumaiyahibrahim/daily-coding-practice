from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            group = nums[i:i+3]
            # Check if the group has 3 elements and fits the condition
            if group[-1] - group[0] > k:
                return []
            res.append(group)
        
        return res
