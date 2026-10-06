from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for j, value in enumerate(nums):
            complement = target - value

            if complement in seen:
                return [seen[complement], j]

            seen[value] = j