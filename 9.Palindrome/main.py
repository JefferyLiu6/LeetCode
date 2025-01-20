class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        palindrome = True
        n = int(len(x)/2)
        for i in range(n+1):
            if x[i-1] != x[-i]:
                palindrome = False
                break
        
        return  palindrome 