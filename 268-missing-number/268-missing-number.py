class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        my_list = set([i for i in range(len(nums) + 1)])
        nums_main = set(sorted(nums))
        left = my_list.difference(nums_main)
        return list(left)[0]