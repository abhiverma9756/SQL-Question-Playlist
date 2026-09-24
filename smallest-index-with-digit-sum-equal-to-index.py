class Solution:
    def smallestIndex(self, a):
        return next((i for i,v in enumerate(a) if sum(map(int,str(v)))==i),-1)
