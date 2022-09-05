from collections import defaultdict, deque

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for idx, val in enumerate(nums):
            dif = target - val
            
            if dif in _dict:
                return [idx, _dict[dif]]
            
            _dict[val] = idx