from time_interval.date import Date
from time_interval.interval import Interval



date_1, date_2 = Date("2020-03-03"), Date("2025-03-13")
print(date_1.all_days)

print(date_1.time)
print(date_1.add_month(11)) # решить проблему с днями
