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
        medianPos = 1+(len(nums1) + len(nums2)) // 2
        even = ((len(nums1) + len(nums2)) % 2 == 0)
        count = 0

        lastElem = []

        pos1 = 0
        pos2 = 0

        while pos1 < len(nums1) or pos2 < len(nums2):
            smallerNum = -1
            if pos1 >= len(nums1):
                smallerNum = nums2[pos2]
                pos2 += 1
            elif pos2 >= len(nums2):
                smallerNum = nums1[pos1]
                pos1 += 1
            else:
                smallerNum = nums2[pos2]
                if nums1[pos1] <= smallerNum:
                    smallerNum = nums1[pos1]
                    pos1 += 1
                else:
                    pos2 += 1

            if len(lastElem) > 0 and not (even and len(lastElem) < 2):
                lastElem.pop(0)
            
            lastElem.append(smallerNum)
            count += 1

            if count == medianPos and not even:
                return lastElem[0]
            elif count == medianPos:
                return sum(lastElem) / 2
            
sol = Solution()
print(sol.findMedianSortedArrays([1,2,3,4,5,14], [6,7,8,9,10,11,12,13]))