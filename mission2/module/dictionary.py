class Dictionary():
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True

            self.week_day = {
                "monday": 0,
                "tuesday": 1,
                "wednesday": 2,
                "thursday": 3,
                "friday": 4,
                "saturday": 5,
                "sunday": 6
            }

            self.grade = {
                "NORMAL": 0,
                "GOLD": 1,
                "SILVER": 2
            }

            self.normal_point = 1
            self.wednesday_point = 3
            self.weekend_point = 2

            self.wednesday_benefit_point = 10
            self.weekend_benefit_point = 10

            self.days_for_get_wednesday_benefit_point = 10
            self.days_for_get_weekend_benefit_point = 10

            self.grade_for_gold = 50
            self.grade_for_silver = 30

dictionary = Dictionary()