
################# Not right solution
# class Solution(object):

# a = ["a","aa"]

# def longestCommonPrefix(strs):
#         compre = ""
#         if(len(strs)) == 0: return compre

#         # compute the min length of strs elements 
#         min = len(strs[0])
#         for i in range(len(strs)-1):
#             if (len(strs[i-1])>len(strs[i])):
#                 min = len(strs[i])


#         for j in range(min):
#             for i in range(1,len(strs)):
#                 if strs[0][j] != strs[i][j]:
#                     return compre
#             compre = compre + strs[0][j]
#         return compre



# print(longestCommonPrefix(a))



############### leetcode reference solution

class Solution(object):

    def longestCommonPrefix(self, strs):
	commonPre = ""

	if len(strs)== 0:
		return commonPre

	for i in range(len(strs[0])):
		for j in range (1,len(strs)):
			if (i >= len(strs[j]) or strs[j][i] != strs[0][i]):
				return commonPre
		commonPre = commonPre + strs[0][i]

	return commonPre