import datetime
import calendar


def create_current_monthly_calendar():
    """Creates a monthly calendar separated by weeks/days"""

    # Grab current month calendar, separate by weeks, and remove weekends
    today = str(datetime.date.today())
    year = today.split('-')[0]
    month = today.split('-')[1]
    year, month = int(year), int(month)

    day_counter = 0
    temp_cal = []
    curr_mon_cal = calendar.Calendar().itermonthdates(year, month)  # months will fill 1st week and start on mondays
    for dates in curr_mon_cal:
        days = str(dates).split('-')[-2:]
        day_counter += 1

        # remove weekends
        if day_counter <= 5:
            temp_cal.append(days)

        if day_counter == 7:
            day_counter = 0

    # separate days into 5 day weeks
    edited_mon_cal = [temp_cal[x:x+5] for x in xrange(0, len(temp_cal), 5)]

    # edited_mon_cal is a 3-d array.

    # edited_mon_cal[0] = [['08', '01'], ['08', '02'], ['08', '03'], ['08', '04'], ['08', '05']]
    # edited_mon_cal[0][0] = ['08', '01']
    # edited_mon_cal[0][0][1] = '01'

    # return monthly_calendar
    return edited_mon_cal


def create_monthly_calendar(year, month):
    """Functions same as create_current_monthly_calendar except given a month
    Month and year are taken as numerals. Ex: 8, 2016 would be August, 2016"""

    day_counter = 0
    temp_cal = []
    curr_mon_cal = calendar.Calendar().itermonthdates(year, month)  # months will fill 1st week and start on mondays
    for dates in curr_mon_cal:
        days = str(dates).split('-')[-2:]
        day_counter += 1

        # remove weekends
        if day_counter <= 5:
            temp_cal.append(days)

        if day_counter == 7:
            day_counter = 0

    # separate days into 5 day weeks
    edited_mon_cal = [temp_cal[x:x + 5] for x in xrange(0, len(temp_cal), 5)]

    # edited_mon_cal is a 3-d array.

    # edited_mon_cal[0] = [['08', '01'], ['08', '02'], ['08', '03'], ['08', '04'], ['08', '05']]
    # edited_mon_cal[0][0] = ['08', '01']
    # edited_mon_cal[0][0][1] = '01'

    # return monthly_calendar
    return edited_mon_cal

