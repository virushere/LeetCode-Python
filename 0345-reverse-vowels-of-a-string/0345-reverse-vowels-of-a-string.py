class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s)-1
        volvelsList = ['a','e','i','o','u','A','E','I','O','U']
        while l<r:
            if s[l] in volvelsList and s[r] in volvelsList:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in volvelsList :
                l = l+1
            elif s[r] not in volvelsList :
                r = r-1
        return ''.join(s)