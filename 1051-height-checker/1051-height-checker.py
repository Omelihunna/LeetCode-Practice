class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        read = range(len(heights))
        exceptions = []
        for i in read:
            if heights[i] != expected[i]:
                exceptions.append(i)
        return len(exceptions)