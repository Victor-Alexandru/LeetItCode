class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0
        g.sort()
        s.sort()
        res = 0
        child_i = 0 
        for cake in s:
            if child_i >= len(g):
                return res
            if cake >= g[child_i]:
                res += 1
                child_i += 1
        
        return res

s = Solution()
print(s.findContentChildren(
    [10, 9, 8, 7], [5, 6, 7, 8]))
