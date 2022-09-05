class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        
        ans = 0
        now = ''
        
        for i in reversed(s):
            if now == '':
                now = i
                continue
            if roman[i] < roman[now]:
                now = i+now
                ans += roman[now]
                now = ''
            else:
                ans += roman[now]
                now = i
        if now != '':
            ans += roman[now]
        
        return ans