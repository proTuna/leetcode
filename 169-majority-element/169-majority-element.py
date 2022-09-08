class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)//2
        _dict = {}
        for i in nums:
            _dict[i] = _dict.get(i,0)+1
        for k,v in _dict.items():
            if v>m:
                return k