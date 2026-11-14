class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        results = dict()
        for num in nums:
            results[num] = 1 + results.get(num, 0)
        
        arr = []
        for num, count in results.items():
            arr.append([count, num])
        
        arr.sort()
        final = []
        while len(final) < k:
            final.append(arr.pop()[1])
        return final
