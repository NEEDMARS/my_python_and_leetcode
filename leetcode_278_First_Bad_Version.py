#278. First Bad Version





# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        while l<r:
            mid=(l+r)//2
            if isBadVersion(mid):
                r=mid-1
            else:
                l=mid+1
        if isBadVersion(l):
            return l
        return l+1
        