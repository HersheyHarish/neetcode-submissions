class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for strings in strs:
            count = [0] * 26
            for ch in strings:
                count[ord(ch) - ord('a')] +=1
            results[tuple(count)].append(strings)
    
        return list(results.values())
        