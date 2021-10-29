DAYS = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

day1 = int(input("First date, day of the month: "))
month1 = int(input("First date, month: "))

day2 = int(input("Second date, day of the month: "))
month2 = int(input("Second date, month: "))

months = month2 - month1

if months == 0:
    result = DAYS[month1] - day1 - (DAYS[month1] - day2)
elif months == 1:
    first_month = DAYS[month1] - day1
    last_month = DAYS[month2] - (DAYS[month2] - day2)
    result = first_month + last_month
else:
    first_month = DAYS[month1] - day1
    last_month = DAYS[month2] - (DAYS[month2] - day2)
    pre_result = 0
    for month in range(month1 + 1, month1 + months):
        pre_result += DAYS[month]
    result = first_month + last_month + pre_result

print(result)