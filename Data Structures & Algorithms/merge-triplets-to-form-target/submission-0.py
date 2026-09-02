class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        aMax = bMax = cMax = False
        for a,b,c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]:
                aMax = True
            if b == target[1]:
                bMax = True
            if c == target[2]:
                cMax = True
        return aMax and bMax and cMax 