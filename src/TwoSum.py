class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {}

        for i in range(len(nums)):
            val = nums[i]
            needed = target - val

            if needed in hmap:
                return [i, hmap[needed]]

            hmap[nums[i]] = i