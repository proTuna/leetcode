class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)
        ans = 0
        for i in columnTitle:
            ans+=26**(l-1)*(ord(i)-64)
            l-=1
        return ans