def is_leap(year):
    """Return True if `year` is a leap year in the Gregorian calendar.

    A year is a leap year if it is divisible by 4, unless it is divisible
    by 100; years divisible by 100 are leap years only if divisible by 400.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
