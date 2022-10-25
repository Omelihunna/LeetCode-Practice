class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        my_dict = {}
        for i, j in enumerate(nums):
            my_dict[i] = abs(j)
        diffs = list(my_dict.values())
        min_diffs = min(diffs)
        home = [k for k, v in my_dict.items() if v == min_diffs]
        if diffs.count(min_diffs) == 1:
            return nums[home[0]]
        else:
            mins = []
            for i in home:
                mins.append(nums[i])
            return max(mins)

            
            
            
        # nums_abs = [abs(i) for i in nums]
        # b = []
        # if nums_abs.count(min(nums_abs)) > 1:
        #     for i in range(len(nums_abs)):
        #         if nums_abs[i] == min(nums_abs):
        #             if nums[i] == nums_abs[i]:
        #                 return nums[i]
        #             else:
        #                 if nums[i] > nums_abs[i]:
        #                     return nums[i]
        #                 else:
        #                     return nums_abs[i]
        # else:
        #     return(min(nums_abs))
            