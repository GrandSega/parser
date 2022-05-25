def convert_time(sec):
    if sec >= 60:
        min = int(sec / 60)
        secunds = sec - (min * 60)
        secunds_str = str(secunds) + " s."

        if min >= 60:
            hours = int(min / 60)
            minuts = min - (hours * 60)
            min_str = str(minuts) + " m. "
            hours_str = str(hours) + " h. "

            if hours >= 24:
                days = int(hours / 24)
                hours = hours - (days * 24)
                hours_str = str(hours) + " h. "
                days_str = str(days) + " d. "
            else:
                hours_str = str(hours) + " h. "
                days_str = ""
        else:
            min_str = str(min) + " m. "
            hours_str = ""

        return days_str + hours_str + min_str + secunds_str
    else:
        return str(sec) + ' s.'


duration = int(input("Укажитеколичество секунд: "))
print(convert_time(duration))