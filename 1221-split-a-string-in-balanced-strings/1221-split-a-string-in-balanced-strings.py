class Solution:
    def balancedStringSplit(self, s: str) -> int:
        _dict = {'R':0,'L':0}
        cnt = 0
        for i in s:
            _dict[i] = _dict.get(i,0)+1
            if _dict['R']==_dict['L']:
                cnt+=1
                _dict['R'],_dict['L']= 0,0
        return cnt