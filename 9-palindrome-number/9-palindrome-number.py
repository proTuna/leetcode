class Solution:
    def isPalindrome(self, x: int) -> bool:
        ans = True
        x = list(str(x))
        l = len(x)
        mid = l//2
        
        for i in range(mid):
            if x[i] != x[l-i-1]:
                ans = False
                break

        return ans