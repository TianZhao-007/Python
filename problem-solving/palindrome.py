####################################solution 1
# def isPalindrome(x):
#         if(x>=0):
#             strg = str(x)
#             strg1 = strg[::-1]
#             if int(strg) == int(strg1):
#                     print("true")
#             else:
#                     print("false")
#         else:
#             print("false")

# while True:
#     x = int(input())
#     isPalindrome(x)

###################### solution 2
x = int(input())
def isPalindrome_1(x):
    return str(x) == str(x)[::-1]

print(isPalindrome_1(x))