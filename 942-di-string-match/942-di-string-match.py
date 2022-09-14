from collections import deque

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = [i for i in range(len(s)+1)]
        q = deque(nums)
        ans = []
        if s[0] == 'I':
            ans.append(q.popleft())
        else:
            ans.append(q.pop())
        for i in range(1,len(s)):
            if s[i-1]=='I' and s[i]=='D':
                ans.append(q.pop())
            elif s[i-1]=='D' and s[i] == 'I':
                ans.append(q.popleft())
            elif s[i-1]=='I' and s[i] == 'I':
                ans.append(q.popleft())
            elif s[i-1] =='D' and s[i] == 'D':
                ans.append(q.pop())
        ans.append(q.pop())
        return ans