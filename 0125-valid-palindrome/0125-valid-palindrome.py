class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        test =  [i.lower() for i in s if i.isalnum() is True]
        print(test)
        palindrome = "".join(test)
        if palindrome[::-1] == palindrome:
            return True
        else:
            return False
        