import calendar

def display_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    print(f"\nCalendar for {month_name} {year}\n")
    print("Mo  Tu  We  Th  Fr  Sa  Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2} ", end="|")
        print()

if __name__ == "__main__":
    year_input = int(input("Enter the year (e.g., 2024): "))
    month_input = int(input("Enter the month (1-12): "))

    display_calendar(year_input, month_input)
