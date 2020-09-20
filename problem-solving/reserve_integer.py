#Given a 32-bit signed integer, reverse digits of an integer.

x = int(input())
def reverse_integer(x):
    if x>=2**31-1 or x<=-2**-31: return 0
    else:
        strg = str(x)
        if x>=0:
             revst = strg[::-1]
        else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
        if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
        else: return int(revst)

print(reverse_integer(x))

# what I learned here
# 1. return has no meaning outside function
# 2. [::-1] is useful when reverse operation is needed
# 3. [a:b] read a place to b-1 place; left get right lose