
# runtime: O(n)
# space:   O(1)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def helper(image, x, y, startcolor, newcolor):
            if (x < 0 or y < 0 or x >= len(image) or y >= len(image[0])
                or image[x][y] != startcolor or image[x][y] == newcolor):
                return

            image[x][y] = newcolor
            helper(image, x + 1, y    , startcolor, newcolor)
            helper(image, x    , y + 1, startcolor, newcolor)
            helper(image, x - 1, y    , startcolor, newcolor)
            helper(image, x    , y - 1, startcolor, newcolor)

        helper(image, sr, sc, image[sr][sc], color)
        return image
