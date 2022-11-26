class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) >= 3:
            for i in range(2):
                main_count = nums.count(max(nums))
                for j in range(main_count):
                    nums.remove(max(nums))
            return max(nums)
        else:
            return max(nums)