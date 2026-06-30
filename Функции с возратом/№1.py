def get_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 11 or month == 9 or  month == 6 or month == 4:
        return 30
    elif month == 2:
        return 28

print(get_days(1))
print(get_days(2))
print(get_days(9))
