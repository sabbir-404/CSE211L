# Function to determine if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Function to get the number of days in a month
def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 30

# Function to get the day of the week for a given date
def day_of_week(year, month, day):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    return (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

# Function to print the calendar
def print_calendar(year, month, day):
    # Print the month and year header
    print(f"{month} {year}")

    # Print the days of the week starting from Sunday
    print("Su Mo Tu We Th Fr Sa")

    # Get the day of the week for the first day of the month
    first_day_of_week = day_of_week(year, month, 1)

    # Determine the number of days in the month
    num_days = days_in_month(year, month)

    # Print leading spaces for the first week
    print("   " * first_day_of_week, end="")

    # Print the days of the month
    for day in range(1, num_days + 1):
        # Print the day with proper padding
        print(f"{day:2}", end=" ")

        # Print a newline if it's the end of the week
        if (day + first_day_of_week) % 7 == 0:
            print()

    # Print a newline if the last day of the month is not the end of the week
    if (num_days + first_day_of_week) % 7 != 0:
        print()

    # Print the day of the week for the specified date
    print(f"The day of the week for {month}/{day}/{year} is {['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][day_of_week(year, month, day)]}")

# Example usage:
year = 2000
month = 1
day = 25

print_calendar(year, month, day)
