class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = []
        my_elements = set(arr)
        for i in my_elements:
            count = arr.count(i)
            if count in counts:
                return False
            else:
                counts.append(count)
                continue              
        return True
            
        