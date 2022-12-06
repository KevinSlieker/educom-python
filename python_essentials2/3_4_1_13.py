class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError
        else:
            self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__number = self.__days.index(self.__day)
        self.__number += n
        self.__daynumber = self.__number % 7
        self.__day = self.__days[self.__daynumber]

    def subtract_days(self, n):
        self.__number = self.__days.index(self.__day)
        self.__number -= n
        self.__daynumber = self.__number % 7
        self.__day = self.__days[self.__daynumber]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")