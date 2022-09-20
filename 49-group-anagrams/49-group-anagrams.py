class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for word in strs:
            ans[''.join(sorted(word))].append(word)
            
        return list(ans.values())