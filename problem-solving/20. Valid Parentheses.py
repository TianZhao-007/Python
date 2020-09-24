# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_bk = ["(","[","{"]
        dic = {")": "(", "}": "{", "]": "["}  # hash map
        stack = ['#']                         # init stack
        for char in s:
            if char in open_bk:
                stack.append(char)
            else:
                if dic[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 1: 
            return True
        else:
            return False
            

# stack data structure to solve this problem...

# 1. pop() delete the last element in the list 
# (e.g. a[1,3,4] -> a.pop() -> meaning that delete a[-1])

# 2. append() add new element for list 
# (e.g. a[1,2,3] -> a.append(2=4) -> a = [1,2,3,4])

