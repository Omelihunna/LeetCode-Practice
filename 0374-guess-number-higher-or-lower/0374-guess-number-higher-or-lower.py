# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r= 1, n                          #     Ex: n = 20  pick = 8
                                            #
        while r >= l:                       #       l     r     m   guess(m)  
                                            #      –––   –––   –––    ––––
            m = (l + r)//2                  #       1     20    10     -1
                                            #       1     10     5     -1
            if   guess(m) ==  1: l = m+1    #       6     10     8     -1
			
            elif guess(m) == -1: r = m      #                    |
										    #                  answer
            else: return m