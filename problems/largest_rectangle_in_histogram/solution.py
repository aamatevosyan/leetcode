class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, st = 0, []
        
        for height in heights + [0]:
            width = 0

            while st and st[-1][1] >= height:
                w, h = st.pop()
                width += w
                res = max(res, width * h)

            st.append((width + 1, height))

        return res