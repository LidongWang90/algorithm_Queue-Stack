# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string],
# where the encoded_string inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
# For example, there will not be input like 3a or 2[4]. Input: s = "3[a2[c]]". Output: "accaccacc
def decod(s):
    res = ""
    stack = []
    num = 0
    prev = ""
    for i in s:
        if i.isalpha():
            res += i
        elif i.isdigit():
            num = num * 10 + int(i)
        elif i == "[":
            stack.append(num)
            stack.append(res)
            num = 0
            res = ""
        elif i == "]":
            res = stack.pop() + stack.pop() * res
    return res


print(decod("10[a2[c]]"))
