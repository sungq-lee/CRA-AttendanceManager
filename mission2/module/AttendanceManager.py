from mission2.module.dictionary import dictionary
from mission2.module.grade import *
from mission2.module.point import *
from mission2.module.benefit import *

class AttendanceManager():
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True

            self.id_cnt = 0
            self.table_id_and_user_name = {}

            # dat[사용자ID][요일]
            self.dat = [[0] * 100 for _ in range(100)]
            self.points = [0] * 100
            self.grade = [0] * 100
            self.names = [''] * 100
            self.wednesday = [0] * 100
            self.weekend = [0] * 100

    def input_user_attendance_info(self, user_name, week_day):
        if user_name not in self.table_id_and_user_name:
            self.id_cnt += 1
            self.table_id_and_user_name[user_name] = self.id_cnt
            self.names[self.id_cnt] = user_name

        user_id = self.table_id_and_user_name[user_name]
        self.get_user_attendance_point(user_id, week_day)

    def get_user_attendance_point(self, user_id, week_day):
        instance_point = factory_point(week_day=week_day)

        add_point = 0
        add_point += instance_point.get_point()

        if week_day == "wednesday":
            self.wednesday[user_id] += 1
        elif week_day == "saturday" or week_day == "sunday":
            self.weekend[user_id] += 1

        self.dat[user_id][instance_point.get_index_week_day()] += 1
        self.points[user_id] += add_point

    def get_wednesday_benefit_point(self):
        instance_benefit = factory_benefit("wednesday")
        for i in range(1, self.id_cnt + 1):
            if self.dat[i][dictionary.week_day["wednesday"]] >= instance_benefit.get_days_for_benefit():
                self.points[i] += instance_benefit.get_benefit_point()

    def get_weekend_benefit_point(self):
        instance_benefit = factory_benefit("weekend")
        for i in range(1, self.id_cnt + 1):
            if (self.dat[i][dictionary.week_day["saturday"]] +
                    self.dat[i][dictionary.week_day["sunday"]] >= instance_benefit.get_days_for_benefit()):
                self.points[i] += instance_benefit.get_benefit_point()

    def calculate_user_grade(self):
        for i in range(1, self.id_cnt + 1):
            instance_grade = factory_grade(self.points[i])
            self.grade[i] = instance_grade.get_grade_index()

            print(f"NAME : {self.names[i]}, POINT : {self.points[i]}, GRADE : ", end="")
            instance_grade.print_grade()


    def calculate_removed_player(self):
        print("\nRemoved player")
        print("==============")
        for i in range(1, self.id_cnt + 1):
            if (self.grade[i] not in (dictionary.grade["GOLD"], dictionary.grade["SILVER"])
                    and self.wednesday[i] == 0 and self.weekend[i] == 0):
                print(self.names[i])

    def execute(self):
        self.get_wednesday_benefit_point()
        self.get_weekend_benefit_point()
        self.calculate_user_grade()
        self.calculate_removed_player()