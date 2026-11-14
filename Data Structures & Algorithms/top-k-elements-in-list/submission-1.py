class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        den = defaultdict(int)

        for num in nums:
            den[num] += 1
        
        ls = []

        for num, cnt in den.items():
            ls.append([cnt,num])
        
        ls.sort()

        ans = []
        while len(ans) < k:
            ans.append(ls.pop()[1])
        
        return ans

        