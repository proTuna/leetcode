class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0],x[1]))
        ans = 0
        cur = 0
        for a,d in properties:
            if d < cur:
                ans+=1
            else:
                cur = d
        return ans