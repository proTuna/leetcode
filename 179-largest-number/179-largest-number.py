class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # numbers = list(map(str, nums))
        # numbers.sort(key=lambda x: x*9, reverse=True)
        # return str(int(''.join(numbers)))
        def swap(n1: int, n2: int) -> bool:
            return str(n1) + str(n2) < str(n2) + str(n1)
        
        i = 1
        while i < len(nums):
            j = i
            while j>0 and swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1
            i+=1
            
        return str(int(''.join(map(str,nums))))