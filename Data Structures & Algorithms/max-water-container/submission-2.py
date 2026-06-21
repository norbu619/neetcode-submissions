class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        res = 0


        for i in range(len(heights)):
            width = right - left
            height = min(heights[left],heights[right])

            if width * height > res:
                res = width*height
            
            if heights[left] > heights[right]:
                right -=1
            elif heights[left] < heights[right]:
                left +=1
            else:
                left +=1

        return res