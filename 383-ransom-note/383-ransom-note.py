class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = True
        
        a = Counter(ransomNote)
        b = Counter(magazine)
        
        for k,v in a.items():
            if k in b and v <= b[k]:
                continue
            else:
                ans = False
                break
                
        return ans