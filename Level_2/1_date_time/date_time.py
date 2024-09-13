from datetime import datetime, timezone

now = datetime.now()
print(now)
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond
print(f"year: {year} month: {month} day: {day} hour: {hour} minute: {minute} second: {second} microsecond: {microsecond}")

date_of_birth = datetime(year=1991, month=2, day=3, hour=7, minute=0, second=0, microsecond=0)
print(f"date_of_birth: {date_of_birth}")


