SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60
seconds = int(input("Пожалуйста введите число: "))
if seconds <= 60:
    print(seconds, 'sec')
else:
    days = seconds // SECONDS_IN_DAY
    seconds = seconds - (days * SECONDS_IN_DAY)
    hours = seconds // SECONDS_IN_HOUR
    seconds = seconds - (hours * SECONDS_IN_HOUR)
    minutes = seconds // SECONDS_IN_MINUTE
    seconds = seconds - (minutes * SECONDS_IN_MINUTE)
    print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds."
      .format(days, hours, minutes, seconds))

