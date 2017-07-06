#Leetcode 207. Course Schedule
#使用广度优先搜索 首先确定哪些课程是第i个课程学习完成后才能学习的
#然后确定在学习第i个课程之前需要学习几门其他课程
#最后遍历；如果没有可以直接学习的课程（即没有限制了的课程）返回False
#有的话 则把该课程学习了，然后将需要学习完该课程然后才能学习的课程的d减一

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        i=0
        res=[]
        d=[]
        while i<numCourses:
            res.append(set())
            d.append(0)
            i+=1
        i=0
        while i<len(prerequisites):
            res[prerequisites[i][1]].add(prerequisites[i][0])
            i+=1
        i=0
        while i<numCourses:
            for it in res[i]:
                d[it]+=1
            i+=1
        i=0
        while i<numCourses:
            j=0
            while j<numCourses:
                if d[j]==0:
                    break
                j+=1
            if j==numCourses:
                return False
            d[j]=-1
            for it in res[j]:
                d[it]-=1
            i+=1
        return True
        