def findNumberofDaysInAMonth(month, year=None):
    month = month.capitalize()
    
    if month == "January":
        return 31
    elif month == "February":
        if year:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                return 29
            else:
                return 28
        else:
            return [28, 29]
    elif month == "March":
        return 31
    elif month == "April":
        return 30
    elif month == "May":
        return 31
    elif month == "June":
        return 30
    elif month == "July":
        return 31
    elif month == "August":
        return 31
    elif month == "September":
        return 30
    elif month == "October":
        return 31
    elif month == "November":
        return 30
    elif month == "December":
        return 31
    else:
        return "Invalid month"

month = input("Enter Month: ")
year = input("Enter Year (optional, press enter to skip): ")
year = int(year) if year else None

days = findNumberofDaysInAMonth(month, year)
print(f"Number of days in {month}: {days}")
