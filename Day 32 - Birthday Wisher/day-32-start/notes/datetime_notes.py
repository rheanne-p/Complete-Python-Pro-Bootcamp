import datetime as dt

# datetime class
# now method: gets current time
now = dt.datetime.now()
print(now) # datetime object

year = now.year  # int
print(year)

if year == 2022:
    print("Wear a face mask")

month = now.month
day_of_week = now.weekday()
print(day_of_week)

# create new datetime object
date_of_birth = dt.datetime(year=2022, month=10, day=15, hour=11)
# hour parameter has ..., since it's a default value

print(date_of_birth)
