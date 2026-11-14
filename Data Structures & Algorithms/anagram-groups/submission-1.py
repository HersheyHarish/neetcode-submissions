class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for val in strs:
            temp = ''.join(sorted(val))
            ans[temp].append(val)
        
        return list(ans.values())
        