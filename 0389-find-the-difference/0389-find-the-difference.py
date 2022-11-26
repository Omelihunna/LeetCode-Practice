class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = [i for i in s]
        t_list = [j for j in t]
        for k in s_list:
            t_list.remove(k)
        return "".join(t_list)
        # mains = [i for i in t if i not in s]
        # mains_string = "".join(mains)
        # return mains_string