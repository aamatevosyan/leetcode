class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        l, r = 0, len(self.calendar) - 1

        while l <= r:
            m = l + (r - l) // 2

            if self.calendar[m][0] > start:
                r = m - 1
            else:
                l = m + 1
        
        if (l - 1 >= 0 and self.calendar[l - 1][1] > start) or (l < len(self.calendar) and self.calendar[l][0] < end):
            return False
        
        self.calendar.insert(l, (start, end))

        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)