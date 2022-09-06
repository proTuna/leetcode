class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        
        for i in range(min(len(word) for word in strs)):
            l = strs[0][i]
            for word in strs[1:]:
                if word[i] != l:
                    return ans
            ans+=l
        
        return ans