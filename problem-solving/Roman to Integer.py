 #Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution(object):
    def romanToInt(self, s):
        sum = 0
        map = {'M':1000, 'D':500,'C':100, 'L':50, 'X':10, 'V':5, 'I':1 }
        for i in range(len(s)-1):
            if map[s[i]]< map[s[i+1]]:
                sum -= map[s[i]]
            else:
                sum += map[s[i]]
        sum += map[s[-1]]

        return sum    
        
# what I learned form this task?
# 1. index of list/dict a = [1,2,3] a[1] = 1; a[2] = 2; a[3] = 3
# 2. s[-1] means the last place of string s
# 3. dictinary is a powful tool 