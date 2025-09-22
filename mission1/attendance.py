from settings import ROOT_DIR

WEEK_DAY = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}

GRADE = {
    "NORMAL": 0,
    "GOLD": 1,
    "SILVER": 2
}

NORMAL_POINT = 1
WEDNESDAY_POINT = 3
WEEKEND_POINT = 2

WEDNESDAY_BENEFIT_POINT = 10
WEEKEND_BENEFIT_POINT = 10

DAYS_FOR_GET_WEDNESDAY_BENEFIT_POINT = 10
DAYS_FOR_GET_WEEKEND_BENEFIT_POINT = 10

GRADE_FOR_GOLD = 50
GRADE_FOR_SLIVER = 30

table_id_and_user_name = {}
id_cnt = 0

# dat[사용자ID][요일]
dat = [[0] * 100 for _ in range(100)]
points = [0] * 100
grade = [0] * 100
names = [''] * 100
wednesday = [0] * 100
weekend = [0] * 100


def get_user_attendance_point(user_id, week_day):
    add_point = 0
    index_week_day = WEEK_DAY[week_day]

    if week_day == "monday":
        add_point += NORMAL_POINT
    elif week_day == "tuesday":
        add_point += NORMAL_POINT
    elif week_day == "wednesday":
        add_point += WEDNESDAY_POINT
        wednesday[user_id] += 1
    elif week_day == "thursday":
        add_point += NORMAL_POINT
    elif week_day == "friday":
        add_point += NORMAL_POINT
    elif week_day == "saturday":
        add_point += WEEKEND_POINT
        weekend[user_id] += 1
    elif week_day == "sunday":
        add_point += WEEKEND_POINT
        weekend[user_id] += 1

    dat[user_id][index_week_day] += 1
    points[user_id] += add_point


def create_new_user(user_name):
    global id_cnt
    if user_name not in table_id_and_user_name:
        id_cnt += 1
        table_id_and_user_name[user_name] = id_cnt
        names[id_cnt] = user_name


def get_wednesday_benefit_point():
    for i in range(1, id_cnt + 1):
        if dat[i][WEEK_DAY["wednesday"]] >= DAYS_FOR_GET_WEDNESDAY_BENEFIT_POINT:
            points[i] += WEDNESDAY_BENEFIT_POINT


def get_weekend_benefit_point():
    for i in range(1, id_cnt + 1):
        if dat[i][WEEK_DAY["saturday"]] + dat[i][WEEK_DAY["sunday"]] >= DAYS_FOR_GET_WEEKEND_BENEFIT_POINT:
            points[i] += WEEKEND_BENEFIT_POINT


def calculate_user_grade():
    for i in range(1, id_cnt + 1):
        if points[i] >= GRADE_FOR_GOLD:
            grade[i] = GRADE["GOLD"]
        elif points[i] >= GRADE_FOR_SLIVER:
            grade[i] = GRADE["SILVER"]
        else:
            grade[i] = GRADE["NORMAL"]

        print(f"NAME : {names[i]}, POINT : {points[i]}, GRADE : ", end="")

        if grade[i] == GRADE["GOLD"]:
            print("GOLD")
        elif grade[i] == GRADE["SILVER"]:
            print("SILVER")
        else:
            print("NORMAL")


def calculate_removed_player():
    print("\nRemoved player")
    print("==============")
    for i in range(1, id_cnt + 1):
        if grade[i] not in (GRADE["GOLD"], GRADE["SILVER"]) and wednesday[i] == 0 and weekend[i] == 0:
            print(names[i])


def input_name_and_day_of_week(user_name, week_day):
    global id_cnt

    create_new_user(user_name)
    user_id = table_id_and_user_name[user_name]
    get_user_attendance_point(user_id, week_day)


def input_and_process_attendance_weekday_500_file(file_path=f"{ROOT_DIR}/attendance_weekday_500.txt"):
    try:
        with open(file_path, encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                name = parts[0]
                day_of_week = parts[1]
                if len(parts) == 2:
                    input_name_and_day_of_week(name, day_of_week)

        get_wednesday_benefit_point()
        get_weekend_benefit_point()
        calculate_user_grade()
        calculate_removed_player()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        raise


if __name__ == "__main__":
    input_and_process_attendance_weekday_500_file()
