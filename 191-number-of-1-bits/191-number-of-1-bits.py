class Solution:
    def hammingWeight(self, n: int) -> int:
        b = '{0:032b}'.format(n)
        ans = b.count('1')
        return ans