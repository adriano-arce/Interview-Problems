from collections import deque


class Scheduler(object):
    def __init__(self, schedule):
        self._schedule = Scheduler.preprocess(schedule)
        print(self._schedule)

    @staticmethod
    def preprocess(schedule):
        sorted_schedule = deque(sorted(schedule))
        merged_schedule = []
        while sorted_schedule:
            start, end = sorted_schedule.popleft()
            while sorted_schedule and end >= sorted_schedule[0][0]:
                garbage, end = sorted_schedule.popleft()
            merged_schedule.append((start, end))
        return merged_schedule

    def is_available(self, meeting):
        low, high = 0, len(self._schedule) - 1
        while low <= high:
            mid = (low + high) // 2
            if self._schedule[mid][0] == meeting[0]:
                return False
            elif self._schedule[mid][0] < meeting[0]:
                low = mid + 1
            else:
                high = mid - 1
        # ASSERT: high and low point to the predecessors/successors of meeting.
        if high >= 0 and self._schedule[high][1] > meeting[0]:
            return False
        if low < len(self._schedule) and self._schedule[low][0] < meeting[1]:
            return False
        return True


def main():
    s1 = [(0, 1), (6, 8), (2, 4), (7, 8), (6, 7), (1, 3), (3, 5)]
    scheduler = Scheduler(s1)
    print('Test Case #1: {}'.format(s1))
    meetings = [(3, 4), (5, 6), (5, 7), (8, 9)]
    for m in meetings:
        print('    {} => {}'.format(m, scheduler.is_available(m)))

if __name__ == "__main__":
    main()