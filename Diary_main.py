import calendar
from Create_Diary_docx import Create_diary
import datetime
from DateFormatter import DateFormatter
from datetime import date
import sys

def month_range(year, month):
    month_name = calendar.month_name[month]
    last_day = calendar.monthrange(year, month)[1]
    start = date(year, month, 1)
    end = date(year, month, last_day)
    return f"{month_name} {start.day}, {year} - {month_name} {end.day}, {year}"

def print_if_none(item):
    if item is not None:
        print(aluan.add_title(item))

if __name__ == '__main__':

    """How to run code
        open terminal tab.
        (PycharmProjects) PS [directory path]> python test0.py arg1 arg2 
    """
    # Print all arguments
    print("Arguments:", sys.argv)

    ref_dt = datetime.datetime(2025, 1, 1)

    if len(sys.argv) < 3:
        raise ValueError("Error: Not enough arguments provided. Usage: python script.py <arg1> <arg2>")

    Y_dt = int(sys.argv[1])
    M_dt = int(sys.argv[2])
    print("First argument:", Y_dt + 2025)
    print("Second argument:", M_dt)
    date_range = month_range(ref_dt.year+Y_dt, ref_dt.month+M_dt)

    print("Date time: ", ref_dt)
    print(date_range)

    fall_2025 = {
        "CSE 101 - Data Structs & Algs":"11:40AM - 1:15PM",
        "CSE 101-02A - Lab Section": "12:35PM - 1:40PM",
        "ECE 129A - Capstone Project I": "5:20PM - 6:55PM",
    }

    weekdays = [
        [1, 3], [2], [0, 2]
    ]

    aluan = Create_diary(
        name=None,
        date=datetime.datetime(ref_dt.year+Y_dt, ref_dt.month+M_dt, 1),
        font_name="Courier New",
        margin_inch=None
    )
    aluan.correct_document_pckg()

    """Set up the title page"""
    aluan.title_page(month_date_range = date_range)

    for D_dt in range(0, 32, 1):
        today = DateFormatter(Y_dt, M_dt, D_dt, ref_dt)

        if (today.dt.month==M_dt+1) is False:
            break

        print(aluan.add_title(today.date_name()))

        print_if_none(today.USA_holidays())
        print_if_none(today.USA_weekday_holidays())

        j = 0
        for key, value in fall_2025.items():
            if D_dt < 7:
                class1 = today.recurring_schedule_entries(class1=f"{value}\n{key}\n", class1_weekdays=weekdays[j])
                print_if_none(class1)
            j += 1
        print(aluan.add_title("\n--------------------\n"))

    aluan.save_diary()