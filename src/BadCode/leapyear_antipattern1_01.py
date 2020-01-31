from datetime import date

def add_years_tp1(d, years):
    return d.replace(year = d.year + years)

def create_date_tp1(d):
    return date(d.year + 1, d.month, d.day)

def is_leap_year_1(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_year_2(year):
    return ((year % 4) and ((year % 100) != 0 or (year % 400) == 0))


def add_years_fp1(d, years):
    if( is_leap_year_1(d.year) and d.month == 2 and d.day == 29 ):
        return d.replace(year = d.year + years, day = 28)
    else:
        return d.replace(year = d.year + years)
