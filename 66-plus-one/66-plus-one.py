class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int("".join(map(str, digits)))
        return list(str(digit+1))