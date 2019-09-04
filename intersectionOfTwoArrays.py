class Solution:
    def intersect(self, nums1, nums2):
        c = list()
        
        for x in nums1:
            if x in nums2:
                nums2.remove(x)
                c.append(x)
        return c


s = Solution()
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
