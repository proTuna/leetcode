class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0],x[1]))
        ans = []
        for i in people:
            h,k = i
            ans.insert(k,[h,k])
        return ans