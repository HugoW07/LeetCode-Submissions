class Solution(object):
    def isPalindrome(self, x):
        string = str(x)
        reversed_x = ""
        for n in string:
            reversed_x = n + reversed_x

        return reversed_x == string
