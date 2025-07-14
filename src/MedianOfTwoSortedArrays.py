class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        median = length // 2

        if length % 2 == 0:
            return (nums[median-1] + nums[median]) / 2
        return nums[median]