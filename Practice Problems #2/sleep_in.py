def sleep_in(weekday, vacation):
    if weekday is False and vacation is False:
        return True
    elif weekday is True and vacation is False:
        return False
    elif weekday is False and vacation is True:
        return True
    else:
        return False


print("True if yes ; False if no.")
w = input("Is it a weekday?\n")
v = input("Is it a vacation?\n")
sleep_in(w, v)
