'''
create last elem queue to store last seen element
counter to count how many items we've seen
calculate median position
check and store whether nums list is even length

use while loop to iterate through both lists until median is reached
    store smaller element in last elem

'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        medianPos = (len(nums1) + len(nums2)) // 2
        merged = nums1 + nums2
        merged.sort()

        if len(merged) % 2 == 0:
            return (merged[medianPos] + merged[medianPos-1])/2
        else:
            return merged[medianPos]
            
sol = Solution()
print(sol.findMedianSortedArrays([1,2,3,4,5,14], [6,7,8,9,10,11,12,13]))