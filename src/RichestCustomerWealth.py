#Beats 100% runtime, O(N) solution, 18.04MB memory
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for lst in accounts:
            wealth = sum(lst)
            if wealth > maxWealth:
                maxWealth = wealth

        return maxWealth
    
#slightly better memory-wise
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for lst in accounts:
            maxWealth = max(sum(lst), maxWealth)

        return maxWealth