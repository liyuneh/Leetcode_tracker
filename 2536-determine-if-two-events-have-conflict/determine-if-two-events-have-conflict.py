class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        if event1[1] == event2[0]:
            return True
        def to_minutes(time:str)->int:
            hh, mm = map(int, time.split(":"))
            return hh* 60 + mm
        start1, end1 = map(to_minutes, event1)
        start2, end2 = map(to_minutes, event2)
        
        return start2 <= end1 and start1 <= end2