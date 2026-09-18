class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l = l + 1
                leftMax = max(leftMax, height[l])
                res = res + (leftMax - height[l])
            else:
                r = r - 1
                rightMax = max(rightMax, height[r])
                res = res + (rightMax - height[r])
        return res
