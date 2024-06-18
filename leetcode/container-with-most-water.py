class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = None

        i = 0
        j = len(height) - 1

        while i < j:
            candidate = min(height[i], height[j]) * (j - i)
            if max is None or max < candidate:
                max = candidate
            
            if height[i] < height[j]:
                x = i
                i += 1
                while height[x] > height[i] and i < j:
                    i += 1
            else:
                x = j
                j -= 1
                while height[x] > height[j] and i < j:
                    j -= 1

        return max
