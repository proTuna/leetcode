class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
                ans.append(prev_elements[:])
                
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()
        dfs(nums)
        return ans