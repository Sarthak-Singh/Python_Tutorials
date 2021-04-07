class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


new = Solution()
print(new.defangIPaddr("1.1.1.1"))
