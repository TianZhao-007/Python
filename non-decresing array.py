#  319 / 334 test cases passed.

# class Solution(object):
#     def checkPossibility(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         count = 0
#         for i in range(len(nums)-1):
#             if(nums[i]>nums[i+1]):
#                 count += 1
        
#         if(count<=1):
#             return true
#         else return false

############### leetcode reference solutoin

# class Solution(object):
#     def checkPossibility(self, A):
#         p = None
#         for i in range(len(A) - 1):
#             if A[i] > A[i+1]:
#                 if p is not None:
#                     return False
#                 p = i

#         return (p is None or p == 0 or p == len(A)-2 or
#                 A[p-1] <= A[p+1] or A[p] <= A[p+2])


##############  CSDN blogger solution(accepted) 
class Solution(object):
    def checkPossibility(self, A):
        one = A[:]
        two = A[:]
        for i in range(len(A)-1):
            if(A[i]>A[i+1]):
                del one[i]
                del two[i+1]
                break
        return two == sorted(two) or one == sorted(one)

        