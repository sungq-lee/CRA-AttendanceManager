import pytest

from settings import ROOT_DIR
from attendance import input_file
from mission2.attendance import input_and_process_attendance_weekday_500_file

from mission2.module.benefit import *
from mission2.module.point import *

def test_original_and_target_output_equal(capsys):
    ## ARRANGE
    input_file(file_path=f"{ROOT_DIR}/attendance_weekday_500.txt")
    captured = capsys.readouterr()
    original_output = captured.out.strip()

    ## ACT
    input_and_process_attendance_weekday_500_file(file_path=f"{ROOT_DIR}/attendance_weekday_500.txt")
    captured = capsys.readouterr()
    target_output = captured.out.strip()

    ## ASSERT
    assert original_output == target_output, "Fail, captured not Equal"


def test_file_not_exist_origin():
    ## ARRANGE
    not_exist_path = f"{ROOT_DIR}/abc.txt"

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        input_file(file_path=not_exist_path)


def test_file_not_exist_target():
    ## ARRANGE
    not_exist_path = f"{ROOT_DIR}/abc.txt"

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        input_and_process_attendance_weekday_500_file(file_path=not_exist_path)


def test_invalid_benefit_week_day():
    ## ARRANGE & Act & Assert
    with pytest.raises(Exception):
        factory_benefit("monday")


def test_invalid_point_week_day():
    ## ARRANGE & Act & Assert
    with pytest.raises(Exception):
        factory_point("someday")
