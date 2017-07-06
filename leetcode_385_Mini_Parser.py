#leetcode 385. Mini Parser
#首先需要判断是不是唯一一个整数  如果是的话 选择直接初始化
#如果是'['则可以确定需要使用add(self, elem)















# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        l=0
        def parseNumber(s,l):
            n=l
            while l<len(s):
                if s[l].isdigit() or s[l]=='-':
                    l+=1
                else:
                    break;
            #print(n,l)
            #print(s[n:l])
            return NestedInteger(int(s[n:l])),l
        def parseList(s,l):
            l+=1
            ans=NestedInteger()
            while l<len(s):
                if s[l]=='[':
                    #print(l)
                    t,l=parseList(s,l)
                    #print(l)
                    ans.add(t)
                elif s[l]=='-' or s[l].isdigit():
                    t,l=parseNumber(s,l)
                    ans.add(t)
                elif s[l]==']':
                    break;
                elif s[l]==',':
                    l+=1
            l+=1
            return ans,l
        if s[l]=='[':
            aa,l=parseList(s,l)
            return aa
        else :
            aa,l=parseNumber(s,l)
            return aa
                