class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        y=x
        if x<0:
            x*=(-1)
        while x != 0:
            digit=x % 10
            rev = rev * 10 + digit
            x=x//10
        if y<0:
            rev*=(-1)
        if -2**31 < rev < 2**31 -1:
            return rev
        else:
            return 0
        