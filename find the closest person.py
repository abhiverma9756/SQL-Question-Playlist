class Solution:
    def findClosest(self, x,y, z):
        d1 = abs(z - x)
        d2 = abs(z - y)

        if d1 < d2:
            return 1
        elif d1 > d2:
            return 2
        else:
            return 0
