class Solution:
    def containsDuplicate(self, nums):
        res = [*set(nums)]
        if len(nums) == len(res):
            return False
        return True
    