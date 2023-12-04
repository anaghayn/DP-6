# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[0 for x in range(n+1)]
        res[0]=1
        p2=p3=p5=0
        n2=2
        n3=3
        n5=5
        for i in range(1,n+1):
            min_num=min(n2,n3,n5)
            res[i]=min_num
            if n2==min_num: 
                p2+=1
                n2=2*res[p2]
            if n3==min_num:
                p3+=1
                n3=3*res[p3]
            if n5==min_num:
                p5+=1
                n5=5*res[p5]
        return res[n-1]
