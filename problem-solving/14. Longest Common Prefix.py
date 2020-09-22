# class Solution(object):

a = ["dog","racecar","car"]

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min = len(strs[0])
        for i in range(len(strs)):
            if (len(strs[i-1])>len(strs[i])):
                min = len(strs[i])


        for j in range(min):
            for i in range(1,len(strs)):
                if strs[0][j] != strs[i][j]:
                    break
        
        if(j == 0): return ""
        else: return strs[0][0:j-1]

print(longestCommonPrefix(a))