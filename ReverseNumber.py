#Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321

class Solution:
    def reverse(self, num):
        revd = int(str(num)[::-1]) if num>= 0 else -int(str(num)[1:][::-1])
        if revd > 2**31 or revd < -2**31:
            return 0
        else:
            return revd
    print(reverse("", 213))