class Solution:
    def capitalizeTitle(self, title: str) -> str:
        test = title.split(" ")
        test_main = [i.title() if len(i) > 2 else i.lower() for i in test]
        result = " ".join(test_main)
        return result