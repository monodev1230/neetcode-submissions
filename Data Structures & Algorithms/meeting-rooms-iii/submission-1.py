from heapq import *

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        # Free rooms: smallest index first
        available = list(range(n))
        heapify(available)

        # Busy rooms: earliest end time, then smallest room index
        busy = []

        roomCounter = [0] * n

        for start, end in meetings:
            duration = end - start

            # Release every room that is free by `start`
            while busy and busy[0][0] <= start:
                endTime, room = heappop(busy)
                heappush(available, room)

            if available:
                # Smallest numbered free room
                room = heappop(available)
                newEnd = end

            else:
                # No free rooms:
                # use room that becomes available earliest
                availableTime, room = heappop(busy)

                newEnd = availableTime + duration

            heappush(busy, (newEnd, room))
            roomCounter[room] += 1

        return max(range(n), key=lambda room: (roomCounter[room], -room))