class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        if len(changed)%2:
            return ans
        changed.sort()
        c = Counter(changed)
        for i in changed:
            if c[i] == 0:
                continue
            else:
                if c.get(i*2,0) >=1:
                    ans.append(i)
                    c[i*2] -=1
                    c[i] -=1
                else:
                    return []
        return ans