class WeekDayError(Exception):
    pass

class Weeker:
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self,day):
        self.day = day

    def __str__(self) -> str:
        return Weeker.week[self.current_day()]

    def add_days(self,n):
        self.day =  Weeker.week[(self.current_day() + n)% 7]

    def subtract_days(self,n):
        self.day = Weeker.week[(self.current_day() - n)% 7]

    def current_day(self):
        
        try:
            Weeker.week.index(self.day)
        except ValueError:
            raise WeekDayError
        
        return Weeker.week.index(self.day)
            



try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
    print(weekday)
except WeekDayError:
    print("Sorry, I can't serve your request.")
