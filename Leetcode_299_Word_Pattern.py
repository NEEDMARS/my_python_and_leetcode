#leetcode 290. Word Pattern
#len 表示长度 
#set(pattern) 将字符串转换为set
#str.split() 将字符串分割成list？split(' ',a) 按空格分割a次，空格按顺序
#zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表。
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=str.split()
        if len(pattern)<len(s):
            return False
        s1=len(set(pattern))
        s2=len(set(s))
        if(s1!=s2):
            return False
        if(s1!=len(set(zip(pattern,s)))):
            return False
        return True