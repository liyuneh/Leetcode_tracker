class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def convert(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(months[:month - 1]) + day

        arrival = convert(arriveAlice)
        arrivalB = convert(arriveBob)

        leave = convert(leaveAlice)
        leaveB = convert(leaveBob)

        mx = max(arrival, arrivalB)
        mn = min(leave, leaveB)

        if mx > mn:
            return 0

        return mn - mx + 1
