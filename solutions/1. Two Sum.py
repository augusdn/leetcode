class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for index, num in enumerate(nums):
            match = target - num
            if match in checked:
                return [checked[match], index]
            else:
                checked[num] = index
