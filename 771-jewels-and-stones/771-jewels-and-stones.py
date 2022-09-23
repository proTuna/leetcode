class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        _dict = {}
        ans = 0
        
        for stone in stones:
            _dict[stone] = _dict.get(stone,0)+1
        
        for jewel in jewels:
            if jewel in _dict:
                ans += _dict[jewel]
                
        return ans