# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums, target):
        seen = {}
        
        for index, num in enumerate(nums):
            other = target - num
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index
        return []

print(twoSum([3,4,2,7,11,15],9))

## What I learned from here??

# 1. enumerate: enumerate is useful for obtaining an indexed list:...
#           (0, seq[0]), (1, seq[1]), (2, seq[2]), ...  

# 2. Hash map: array + linked list
#     value_Position = F(keys), we only need to search keys to get the value_Position
#     One to one map relationship;
#     contiunous storage space to store Hash map;
#     There is no relationship between elements;
#     collision/conflicts may occur(e.g. key1!=key2, but f(key1) = f(key2));


 