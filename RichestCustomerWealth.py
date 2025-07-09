#Beats 100% runtime, O(N) solution, 18.04MB memory
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0

        for lst in accounts:
            wealth = sum(lst)
            if wealth > max:
                max = wealth

        return max