# ----------------------------------------
# Schedule Entry Formatter Template
#
# Description: Python utility for formatting daily schedule entries with dates.
#              Converts date calculations into formatted output for work and class schedules.
#              Originally converted from Windows PowerShell script.
#
# Usage: Customize the recurring events and time ranges in the main section
#        to generate formatted schedule entries for any date range.
#
# Date Created: August 2025
# ----------------------------------------

import datetime
from dateutil.relativedelta import relativedelta

class DateFormatter:
    def __init__(self, Y_dt=0, M_dt=0, D_dt=0, ref_dt=None):
        if ref_dt == None:
            ref_dt = datetime.datetime.today()
        self.dt = ref_dt + relativedelta(years=Y_dt, months=M_dt, days=D_dt)

    def current_time_tf(self):
        rn = datetime.datetime.today()
        date_rn = [self.dt.year, self.dt.month, self.dt.day]
        date_ref = [rn.year, rn.month, rn.day]
        tf = []
        statement = 1
        for i in range(0,3):
            # print(f"{date_rn[i]}=={date_ref[i]}:", date_rn[i] == date_ref[i])
            tf.append(date_rn[i] == date_ref[i])
            statement = statement * tf[i]
        return statement


    def date_name(self):
        final_dt = datetime.datetime(self.dt.year, self.dt.month, self.dt.day)
        return final_dt.strftime("%A, %B %d, %Y")

    def ISO_week_number(self):
        week_number = self.dt.isocalendar()[1]
        return week_number

    def USA_holidays(self):
        if (int(self.dt.month) == 1) and (int(self.dt.day) == 1):
            return "New Year's Day"
        elif (int(self.dt.month) == 7) and (int(self.dt.day) == 4):
            return "U.S.A. Independence Day"
        elif (int(self.dt.month) == 10) and (int(self.dt.day) == 31):
            return "Halloween"
        elif (int(self.dt.month) == 12) and (int(self.dt.day) == 24):
            return "Christmas Eve"
        elif (int(self.dt.month) == 12) and (int(self.dt.day) == 25):
            return "Christmas Day"
        elif (int(self.dt.month) == 12) and (int(self.dt.day) == 31):
            return "New Year's Eve"
        else:
            return None

    def USA_weekday_holidays(self):
        weeknum = int(DateFormatter.ISO_week_number(self))
        if (self.dt.weekday() == 1) and (weeknum == 4):
            return "Martin Luther King Jr. Day"
        elif (self.dt.weekday() == 0) and (weeknum == 8):
            return "Washington's Birthday"  # 3rd Monday in February
        elif (self.dt.weekday() == 0) and (weeknum == 22):
            return "Memorial Day"  # Last Monday in May
        elif (self.dt.weekday() == 0) and (weeknum == 36):
            return "Labor Day"  # 1st Monday in September
        elif (self.dt.weekday() == 0) and (weeknum == 42):
            return "Columbus Day / Indigenous Peoples' Day"  # 2nd Monday in October
        elif (self.dt.weekday() == 3) and (weeknum == 48):
            return "Thanksgiving Day"
        else:
            return None

    # weekday input examples:
    #   Monday(0)   Tuesday(1)      Wednesday(2)    Thursday(3)     Friday(4)   Saturday(5)     Sunday(6)
    # class1_weekdays is a list, like [0, 2, 4] and [1, 3]

    def recurring_schedule_entries(self, class1, class1_weekdays):
        """
        Print recurring event details if the current date falls on specified weekdays.

        Args:
            class1 (str): Description of the recurring event
            class1_weekdays (list): List of weekday numbers (Monday=0, Sunday=6)

        Example:
            recurring_schedule_entries("Team Meeting", [1, 3])
            Prints "Team Meeting" if today's date falls on Tuesday or Thursday
        """
        for weekday in class1_weekdays:
            if self.dt.weekday() == int(weekday):
                return f"{class1}\n"
            return None

def main():
    for i in range(0, 14):  # Adjust range as needed (days 22–140 from reference date)

        # Create a new schedule formatter for each day
        schedule_formatter = DateFormatter(0, 0, i, ref_dt)

        # Print the formatted date
        print("📅", schedule_formatter.date_name())

        # Add recurring events based on weekday
        schedule_formatter.recurring_schedule_entries("12:00PM - 2:20PM\nClass Session", [1, 3])  # Tuesdays & Thursdays
        schedule_formatter.recurring_schedule_entries("9:00AM - 10:20AM\nWork Shift", [0, 2])     # Mondays & Wednesdays

        print("--------------------\n")


# ========================================
# MAIN CONFIGURATION SECTION
# ========================================

if __name__ == '__main__':

    try:
        document = Document(foo='bar', baz=12)
        print(document['baz'])

    except:
        print("Old Document class is gone — this failed as expected.\n")

    # Set your reference starting date (change as needed)
    ref_dt = datetime.datetime(2020, 1, 1, 0, 0, 0)
    print("Reference date:", ref_dt.strftime("%A, %B %d, %Y"))

    # ---- CUSTOMIZE YOUR SCHEDULE ----
    # Weekday reference: Monday(0) Tuesday(1) Wednesday(2) Thursday(3) Friday(4) Saturday(5) Sunday(6)

    # Example: Generate schedule entries for a date range
    # Change the range and events below to match your needs
    main()

"""
========================================
USAGE EXAMPLES:
========================================

1. Generate a single formatted date:
   DateFormatter.date_name(0, 1, 15)  # 1 month, 15 days from reference

2. Show all dates in a month:
   DateFormatter.date_month("name", 0, 2)  # Show month 2 from reference year

3. Find holidays in a year:
   DateFormatter.USA_holidays(1)  # Show holidays 1 year from reference

4. Add custom recurring events:
   DateFormatter.recurring_schedule_entries(0, 0, i, "Custom Event", [0, 2, 4])  # Monday, Wednesday, Friday

5. Common weekday patterns:
   [0, 1, 2, 3, 4] = Weekdays (Monday-Friday)
   [5, 6] = Weekends (Saturday-Sunday)
   [1, 3] = Tuesday, Thursday
   [0, 2, 4] = Monday, Wednesday, Friday
========================================
"""