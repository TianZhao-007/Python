#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and 
# returns the new length.
# Do not allocate extra space for another array, you must do this
#  by modifying the input array in-place with O(1) extra memory

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dif_num = 1
        if nums == []:
             return 0
        for i in range(len(nums)):
            if(i+1<len(nums)):
                if nums[i]<nums[i+1]:
                    nums[dif_num] = nums[i+1]
                    dif_num += 1 
        print(nums)
        return dif_num
    