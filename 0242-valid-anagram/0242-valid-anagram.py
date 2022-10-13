class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test_s = [i for i in s]
        test_t = [j for j in t]
        if sorted(test_s) == sorted(test_t):
            return True
        return False