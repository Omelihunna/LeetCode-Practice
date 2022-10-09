class Solution:
    def isHappy(self, n: int) -> bool:
        x = str(n)
        if x == "1":
            return True
        while x != "1":
            n_list_squared = [(int(i)** 2) for i in x]
            x = str(sum(n_list_squared))
            if x == "145":
                return False
        if x == "1":
            return True  
        