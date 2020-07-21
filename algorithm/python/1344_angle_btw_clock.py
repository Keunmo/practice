# https://leetcode.com/problems/angle-between-hands-of-a-clock/submissions/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_d = 30 * (hour % 12) + (minutes * 0.5)
        min_d = minutes * 6
        return min(max(min_d - hour_d, hour_d - min_d), 360-max(min_d - hour_d, hour_d - min_d))