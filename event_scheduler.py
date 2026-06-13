#Problem 2: Event Scheduler 
import heapq


def can_attend_all(events):
    """
    Returns True if no events overlap.
    """

    if not events:
        return True

    events = sorted(events, key=lambda x: x[0])

    for i in range(1, len(events)):
        prev_end = events[i - 1][1]
        curr_start = events[i][0]

        if curr_start < prev_end:
            return False

    return True


def min_rooms_required(events):
    """
    Returns minimum number of meeting rooms required.
    """

    if not events:
        return 0

    events = sorted(events, key=lambda x: x[0])

    min_heap = []
    max_rooms = 0

    for start, end in events:

        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, end)

        max_rooms = max(max_rooms, len(min_heap))

    return max_rooms


# Example Usage

events1 = [(9, 10), (10, 11), (11, 12)]

print("Can attend all:", can_attend_all(events1))
print("Rooms required:", min_rooms_required(events1))

events2 = [(9, 11), (10, 12), (11, 13)]

print("Can attend all:", can_attend_all(events2))
print("Rooms required:", min_rooms_required(events2))
