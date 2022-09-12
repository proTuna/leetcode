class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numbers = list(map(str, nums))
        numbers.sort(key=lambda x: x*9, reverse=True)
        return str(int(''.join(numbers)))