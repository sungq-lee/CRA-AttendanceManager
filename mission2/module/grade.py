from abc import ABC, abstractmethod
from mission2.module.dictionary import dictionary


class Grade(ABC):
    @abstractmethod
    def print_grade(self):
        pass

    @abstractmethod
    def get_grade_index(self):
        pass


class Gold(Grade):
    def print_grade(self):
        print("GOLD")

    def get_grade_index(self):
        return dictionary.grade["GOLD"]


class Silver(Grade):
    def print_grade(self):
        print("SILVER")

    def get_grade_index(self):
        return dictionary.grade["SILVER"]


class Normal(Grade):
    def print_grade(self):
        print("NORMAL")

    def get_grade_index(self):
        return dictionary.grade["NORMAL"]


def factory_grade(point: int) -> Grade:
    if point >= dictionary.grade_for_gold:
        return Gold()
    elif point >= dictionary.grade_for_silver:
        return Silver()
    else:
        return Normal()
