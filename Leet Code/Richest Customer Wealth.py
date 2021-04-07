class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for x in accounts:
            if sum(x) > richest:
                richest = sum(x)
        return richest