class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0     
        for i in points:
            d = {}
            for j in points:
                dist = (i[0]-j[0])**2 + (i[1]-j[1])**2
                print dist
                d[dist] = d.get(dist, 0) + 1
                
            for n in d:
                res += d[n] * (d[n]-1)
                print '-'*10
                print res
        return res
