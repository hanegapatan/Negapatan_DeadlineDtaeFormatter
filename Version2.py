import datetime

# Version 2: Added date formatting

# 1. Inputs
event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# 2. Date Processing
event_date = datetime.date(year, month, day)

# 3. Outputs matching the sample format
print("\nFormatted Output:")
print(f"Event: {event_title.upper()}")
print(f"Date: {event_date.strftime('%B %d, %Y')}")
print(f"Year: {event_date.strftime('%Y')}")
print(f"Month: {event_date.strftime('%B')}")
print(f"Day: {event_date.strftime('%d').lstrip('0')}")
print(f"Weekday: {event_date.strftime('%A')}")
