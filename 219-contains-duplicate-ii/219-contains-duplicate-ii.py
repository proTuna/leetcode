class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        _dict = {}
        for i,v in enumerate(nums):
            if v in _dict and i-_dict[v] <=k:
                return True
            _dict[v] = i
        return False