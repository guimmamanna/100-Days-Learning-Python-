def life_in_weeks(age):
    live_until = 90 * 52
    week = age * 52
    print(
        f" For age {age}, there should be {live_until - week} weeks remaining")


life_in_weeks(20)
