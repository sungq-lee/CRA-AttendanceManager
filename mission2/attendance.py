from settings import ROOT_DIR

from mission2.module.AttendanceManager import AttendanceManager

def input_and_process_attendance_weekday_500_file(file_path=f"{ROOT_DIR}/attendance_weekday_500.txt"):
    try:
        attendance_manager = AttendanceManager()
        with open(file_path, encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                name = parts[0]
                day_of_week = parts[1]
                if len(parts) == 2:
                    attendance_manager.input_user_attendance_info(name, day_of_week)

            attendance_manager = AttendanceManager()
            attendance_manager.execute()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        raise



if __name__ == "__main__":
    input_and_process_attendance_weekday_500_file()

