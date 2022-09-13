class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        odd = 0
        _dict = {}
        for i in s:
            _dict[i] = _dict.get(i,0)+1
        for k,v in _dict.items():
            ans += (v//2)*2
            if v%2 != 0:
                odd = 1
        ans += odd
        return ans