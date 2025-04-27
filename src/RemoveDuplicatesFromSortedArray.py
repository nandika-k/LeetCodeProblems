class Solution(object):
    def removeDuplicates(self, nums):
        curr_digit = None
        index = 0
        while True:
            if index >= len(nums):
                break
            if curr_digit is not None and nums[index] == curr_digit:
                nums.pop(index)
                index -= 1
            else:
                curr_digit = nums[index]
            index += 1
        return len(nums)
        