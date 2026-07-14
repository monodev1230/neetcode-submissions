class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boatCount = 0
        while left < right: #!
            if people[left] + people[right] > limit:
                right -= 1
            else:
                right -= 1
                left += 1
            boatCount +=1
        if left == right:
            boatCount += 1
        return boatCount