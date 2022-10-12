class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        if n == 0:
            return False
        if n == 1:
            return True
        while n % 2 == 0:
            n /= 2            
        return n == 1