#leetcode 434.Number of Segments in a String
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0:
            return 0
        i=0
        ans=0
        while i<n and s[i]==' ':
            i+=1
        while i<n:
            if s[i]==' ' and s[i-1] != ' ':
                ans+=1
            i+=1
        if s[n-1]!=' ':
            ans+=1
        return ans