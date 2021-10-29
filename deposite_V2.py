params_key = ["deposit", "interest", "days"]
params = {"deposit":None, "interest":None, "days":None}

def deposit():
    for param in params_key:
        params[param] = input('Tell me your {}: '.format(param))
        try:
            float(params[param])
        except Exception:
            print("Sometning went wrong with your input.")
            asking()
    
    year_days = 365

    year_income = float(params["deposit"]) * (float(params["interest"]) * 0.01)
    income = year_income * (float(params["days"]) / float(year_days))

    print("You will earn {} for one year".format(year_income))
    print("You have earned {} for {} days".format(income, params["days"]))

    asking()

def asking():
    if (input("Wanna try it again? (type 'Yes' if you want): ")).lower().strip() == "yes":
        deposit()
    else:
        exit()

deposit()