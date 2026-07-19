class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:    
        N = mountainArr.length()

        l, r = 0, N - 1
        while l < r:
            m = (r-l)//2 + l
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l

        l, r = 0, peak
        while l <= r:
            m = (r-l)//2 + l
            midVal = mountainArr.get(m)
            if midVal == target:
                return m
            elif midVal < target:
                l = m + 1
            else:
                r = m - 1
        l, r = peak + 1, N - 1
        while l <= r:
            m = (r-l)//2 + l
            midVal = mountainArr.get(m)
            if midVal == target:
                return m
            elif midVal < target:
                r = m - 1
            else:
                l = m + 1
        return -1
