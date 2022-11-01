class Solution:
    def isPalindrome(self, s: str) -> bool:
        test =  [i.lower() for i in s if i.isalnum() is True]
        print(test)
        palindrome = "".join(test)
        if palindrome[::-1] == palindrome:
            return True
        else:
            return False
        