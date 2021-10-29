def deposit():
    deposit = input('Tell me your deposit: ')
    interest = input('Tell me your interest: ')
    days = input("Tell me your deposit's time (in days): ")
    year_days = 365

    try:
        float(deposit)
        float(interest)
        float(days)
    except Exception:
        print("Sometning went wrong with your input.")
        asking()

    year_income = float(deposit) * (float(interest) * 0.01)
    income = year_income * (float(days) / float(year_days))

    print("You will earn {} for one year".format(year_income))
    print("You have earned {} for {} days".format(income, days))

    asking()

def asking():
    if (input("Wanna try it again? (type 'Yes' if you want): ")).lower().strip() == "yes":
        deposit()
    else:
        exit()

deposit()