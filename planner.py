from bisect import bisect_left
import time

class TimePeriod:
    start: float
    end: float

    def __init__(self, start: float, end: float) -> None:
        self.start = start
        self.end = end

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, TimePeriod):
            return False
        return self.start < other.start

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TimePeriod):
            return False
        return self.start == other.start and self.end == other.end

    def contains(self, other: object) -> bool:
        if not isinstance(other, TimePeriod):
            return False
        return self.start <= other.start and self.end >= other.end

class Group:
    count: int
    next_available: float
    limit: TimePeriod

    def __init__(self, count: int, limit: TimePeriod) -> None:
        self.count = count
        self.next_available = limit.start
        self.limit = limit

class Court:
    time_available: list[TimePeriod]

    def __init__(self, available: list[TimePeriod]) -> None:
        self.time_available = available
        self.time_available.sort()

    def get_available_periods(self, limit: TimePeriod | None) -> list[TimePeriod]:
        if limit is None:
            return self.time_available
        start = bisect_left(self.time_available, limit)
        if start >= len(self.time_available) or self.time_available[start].start >= limit.end:
            return []
        end = len(self.time_available)
        for i in range(start + 1, len(self.time_available)):
            if self.time_available[i].start >= limit.end:
               end = i
        return self.time_available[start:end]

    def book_period(self, period: TimePeriod) -> bool:
        idx = bisect_left(self.time_available, period)
        if idx >= len(self.time_available):
            return False
        if self.time_available[idx].start > period.start or self.time_available[idx] < period.end:
           return False

        if period == self.time_available[idx]:
            self.time_available.pop(idx)
        elif period.end == self.time_available[idx].end:
            self.time_available[idx].end = period.start
        elif period.start == self.time_available[idx].start:
            self.time_available[idx].start = period.end
        else:
            end = self.time_available[idx].end
            self.time_available[idx].end = period.start
            self.time_available.insert(idx + 1, TimePeriod(period.end, end))
        return True

    def unbook_period(self, period: TimePeriod):
        idx: int = bisect_left(self.time_available, period)
        if (idx > 0 and self.time_available[idx - 1].contains(period)) or (idx < len(self.time_available) and self.time_available[idx].contains(period)):
            return

        insert: TimePeriod = period
        if idx > 0 and self.time_available[idx - 1].end >= period.start:
            insert.start = self.time_available[idx - 1].start
            self.time_available.pop(idx - 1)
            idx -= 1

        while idx < len(self.time_available) and self.time_available[idx].end <= insert.end:
            self.time_available.pop(idx)

        self.time_available.insert(idx, insert)


class Solver:
    groups: list[Group]
    courts: list[Court]
    rest_time: float
    evaluate_time: float

    def __init__(self, groups: list[Group], courts: list[Court], rest_time, evaluate_time) -> None:
        self.groups = groups
        self.courts = courts
        self.rest_time = rest_time
        self.evaluate_time = evaluate_time

    def find_timetable(self):
        pass

    def _find_timetable_recursive(self, idx: int):
        pass
