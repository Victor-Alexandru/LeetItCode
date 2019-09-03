class Solution:
    def defangIPaddr(self, address):
        return address.replace('.','[.]') 


s = Solution()
print(s.defangIPaddr("1.1.1.1.1"))