from abc import ABC, abstractmethod
from mission2.module.dictionary import dictionary

class Point(ABC):
    @abstractmethod
    def get_point(self):
        pass

    @abstractmethod
    def get_index_week_day(self):
        pass


class PointMonday(Point):
    def get_point(self):
        return dictionary.normal_point

    def get_index_week_day(self):
        return dictionary.week_day["monday"]

class PointTuesday(Point):
    def get_point(self):
        return dictionary.normal_point

    def get_index_week_day(self):
        return dictionary.week_day["tuesday"]

class PointWednesday(Point):
    def get_point(self):
        return dictionary.wednesday_point

    def get_index_week_day(self):
        return dictionary.week_day["wednesday"]

class PointThursday(Point):
    def get_point(self):
        return dictionary.normal_point

    def get_index_week_day(self):
        return dictionary.week_day["thursday"]

class PointFriday(Point):
    def get_point(self):
        return dictionary.normal_point

    def get_index_week_day(self):
        return dictionary.week_day["friday"]

class PointSaturday(Point):
    def get_point(self):
        return dictionary.weekend_point

    def get_index_week_day(self):
        return dictionary.week_day["saturday"]

class PointSunday(Point):
    def get_point(self):
        return dictionary.weekend_point

    def get_index_week_day(self):
        return dictionary.week_day["sunday"]


def factory_point(week_day: str) -> Point:
    if week_day == "monday":
        return PointMonday()
    elif week_day == "tuesday":
        return PointTuesday()
    elif week_day == "wednesday":
        return PointWednesday()
    elif week_day == "thursday":
        return PointThursday()
    elif week_day == "friday":
        return PointFriday()
    elif week_day == "saturday":
        return PointSaturday()
    elif week_day == "sunday":
        return PointSunday()
    else:
        raise Exception("Invalid week_day. Input ex)  monday, tuesday, wednesday, thursday, friday, saturday, sunday")

