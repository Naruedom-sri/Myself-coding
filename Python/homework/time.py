print(" *** Transform second ***")
second = input('Enter seconds : ')
dot = 0
comma = ""
for i in second:
    if i == ".":
        dot += 1
    else:
        if i == '_':
            comma += ","
        else:
            comma += i
if dot >= 1:
    print("! ! ! please enter a whole number ==>", second)
else:
    second_int = int(second)
    minute_int = int(second_int / 60)
    hour_int = int(second_int / 3600)
    day_int = int(second_int / 86400)
    week_int = int(second_int / 604800)
    # second
    if second_int < 60:
        print(comma, "seconds ==> ", second, "seconds")
    # minute
    elif second_int < 3600:
        if second_int % 60 == 0:
            print(comma, "seconds ==> ", minute_int, "minutes")

        else:
            print(comma, "seconds ==> ", minute_int,
                  "minutes", second_int % 60, "seconds")

    # hour
    elif second_int < 86400:
        if second_int % 3600 == 0:
            print(comma, "seconds ==> ", hour_int, "hours")

        elif minute_int % 60 != 0 and second_int % 60 != 0:
            print(comma, "seconds ==> ", hour_int, "hours",
                  minute_int % 60, "minutes", second_int % 60, "seconds")

        else:
            print(comma, "seconds ==> ", hour_int,
                  "hours", minute_int % 60, "minutes")

    # day
    elif second_int < 604800:
        if second_int % 86400 == 0:
            print(comma, "seconds ==> ", day_int, "days")

        elif hour_int % 24 != 0 and minute_int % 60 == 0 and second_int % 60 == 0:
            print(comma, "seconds ==> ", day_int,
                  "days", hour_int % 24, "hours")

        elif hour_int % 24 == 0 and minute_int % 60 != 0 and second_int % 60 == 0:
            print(comma, "seconds ==> ", day_int,
                  "days", minute_int % 60, "minutes")

        elif hour_int % 24 == 0 and minute_int % 60 == 0 and second_int % 60 != 0:
            print(comma, "seconds ==> ", day_int,
                  "days", second_int % 60, "seconds")

        elif hour_int % 24 == 0 and minute_int % 60 != 0 and second_int % 60 != 0:
            print(comma, "seconds ==> ", day_int, "days", minute_int %
                  60, "minutes", second_int % 60, "seconds")

        elif hour_int % 24 != 0 and minute_int % 60 != 0 and second_int % 60 == 0:
            print(comma, "seconds ==> ", day_int, "days", hour_int % 24,
                  "hours", minute_int % 60, "minutes")

        elif hour_int % 24 != 0 and minute_int % 60 == 0 and second_int % 60 != 0:
            print(comma, "seconds ==> ", day_int, "days", hour_int % 24,
                  "hours", second_int % 60, "seconds")

        else:
            print(comma, "seconds ==> ", day_int, "days", hour_int % 24,
                  "hours", minute_int % 60, "minutes", second_int % 60, "seconds")

    # week
    else:
        if second_int % 604800 == 0:
            print(comma, "seconds ==> ", week_int, "weeks")

        else:
            if day_int % 7 != 0 and hour_int % 24 == 0 and minute_int % 60 == 0 and second_int % 60 == 0:
                print(comma, "seconds ==> ", week_int, "weeks", day_int % 7,
                      "days")

            elif day_int % 7 == 0 and hour_int % 24 != 0 and minute_int % 60 == 0 and second_int % 60 == 0:
                print(comma, "seconds ==> ", week_int, "weeks", hour_int % 24,
                      "hours")

            elif day_int % 7 == 0 and hour_int % 24 == 0 and minute_int % 60 != 0 and second_int % 60 == 0:
                print(comma, "seconds ==> ", week_int, "weeks",  minute_int % 60,
                      "minutes")

            elif day_int % 7 == 0 and hour_int % 24 == 0 and minute_int % 60 == 0 and second_int % 60 != 0:
                print(comma, "seconds ==> ", week_int, "weeks",  second_int % 60,
                      "seconds")

            elif day_int % 7 != 0 and hour_int % 24 != 0 and minute_int % 60 == 0 and second_int % 60 == 0:
                print(comma, "seconds ==> ", week_int, "weeks", day_int % 7,
                      "days", hour_int % 24, "hours")

            elif day_int % 7 != 0 and hour_int % 24 == 0 and minute_int % 60 != 0 and second_int % 60 == 0:
                print(comma, "seconds ==> ", week_int, "weeks", day_int % 7,
                      "days",  minute_int % 60, "minutes")

            elif day_int % 7 != 0 and hour_int % 24 == 0 and minute_int % 60 == 0 and second_int % 60 != 0:
                print(comma, "seconds ==> ", week_int, "weeks", day_int % 7,
                      "days", second_int % 60, "seconds")

            elif day_int % 7 != 0 and hour_int % 24 != 0 and minute_int % 60 != 0 and second_int % 60 == 0:
                print(comma, "seconds ==> ", week_int, "weeks", day_int % 7,
                      "days", hour_int % 24, "hours", minute_int % 60, "minutes")

            elif day_int % 7 != 0 and hour_int % 24 != 0 and minute_int % 60 == 0 and second_int % 60 != 0:
                print(comma, "seconds ==> ", week_int, "weeks", day_int % 7,
                      "days", hour_int % 24, "hours", second_int % 60, "seconds")

            else:
                print(comma, "seconds ==> ", week_int, "weeks", day_int % 7,
                      "days", hour_int % 24, "hours", minute_int % 60, "minutes", second_int % 60, "seconds")
print(" --- program end ---")
