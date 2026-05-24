# Problem: Two Sum
# Platform: neetcode
# Difficulty: Easy
# Language: python
# Synced: 2026-05-24T04:17:27.540Z
Code  |  PythonVisualize codeShare Solutionclass Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [hash[complement], i]
            hash[num] = i
        return []