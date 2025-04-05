class Solution(object):
    def maxArea(self, height):
        length = len(height)
        ls = []
        for r in range(length):
            for l in range(length):
                ls.append((length-r)* min(height[l], height[r]))
        return max(ls)
       