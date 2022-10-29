class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        count = 0
        test = ""
        while goal != test and count < len(s):
            test = s[count:] + s[:count]
            count += 1
        if goal == test:
            return True
        else:
            return False