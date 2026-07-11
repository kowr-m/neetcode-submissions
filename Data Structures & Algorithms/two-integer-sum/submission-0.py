class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, x in enumerate(nums):
            find = target-x
            for j, y in enumerate(nums):
                if j <= i:
                    continue
                if y == find:
                    return [i,j]