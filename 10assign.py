def trouble(talk,hour):
    if hour in range(0,24):
        if hour<7 or hour>20:
            if talk:
                return True
            else:
                return False
        else:
            return False
    else:
        print("only 24 hours per day")

print(trouble(True,6))