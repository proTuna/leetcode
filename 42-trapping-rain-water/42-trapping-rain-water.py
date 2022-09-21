class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[0], height[right]
        
        while left<right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                ans += left_max - height[left]
                left+=1
            else:
                ans += right_max - height[right]
                right -=1
            
        return ans