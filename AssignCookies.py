class Solution:
    def findContentChildren(self, g, s) -> int:
        g = sorted(g)
        s = sorted(s)
        total_cookies = 0
        greed_max = max(g)
        size_max = max(s)
        if greed_max < size_max:
            return min(len(g), len(s))
        size_index = 0
        for greed in g:
               if size_index > len(s):
                      break
               if greed <= s[size_index]:
                      size_index += 1
                      total_cookies += 1
               else:
                      return total_cookies
        return total_cookies


s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))
