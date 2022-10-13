class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = nums.count(0)
        for i in range(a):
            nums.remove(0)
        for i in range(a):
            nums.append(0)
        return nums