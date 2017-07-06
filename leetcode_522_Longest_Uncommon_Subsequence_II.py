#leetcode 522 Longest Uncommon Subsequence II 
#代码太长....定义一个函数  判断s1是不是s2的子序列（len(s1)<len(s2)）
#再写两个循环 如果s1是s2的子序列 删除s1，如果s1==s2 删除s1和s2
#则最终剩下的最长的字符串就是所求答案

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def subseq(s1,s2):
            i=0
            for it in s2:
                if i<len(s1) and s1[i]==it:
                    i+=1
            return i==len(s1)
        i=0
        strs.sort(key=len,reverse=False)
        while i<len(strs):
            b=False
            j=i+1
            while j<len(strs):
                if subseq(strs[i],strs[j]):
                    b=True
                    if len(strs[i])==len(strs[j]):
                        strs.pop(j)
                    else:
                        j+=1
                else:
                    j+=1
            if b:
                strs.pop(i)
            else:
                i+=1
        if len(strs)==0:
            return -1
        return len(strs[-1])