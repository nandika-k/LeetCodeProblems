class Solution:
    def longestConsecutive(self, nums) -> int:
        nums = set(nums)
        maxSeq = 0

        for num in nums:
            length = 0
            if (num-1) not in nums:
                length = 1

                while (num+1) in nums:
                    num += 1
                    length += 1
                maxSeq = max(maxSeq, length)
        return maxSeq


sol = Solution()
print(sol.longestConsecutive([2,20,4,10,3,4,5]))