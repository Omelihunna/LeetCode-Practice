class Solution:
    def isHappy(self, n: int) -> bool:
        sum_of_squares = 0
        x = str(n)
        if x == "2":
            return False
        if x == "1":
            return True
        while x != "1":
            n_list_squared = [(int(i)** 2) for i in x]
            x = str(sum(n_list_squared))
            if x == "145":
                return False
        if x == "1":
            return True  
        