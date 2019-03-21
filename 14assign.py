def sleep_in(weekday,vacation):
    if not weekday and not vacation:
        return True
    elif not weekday and vacation:
        return True
    #elif weekday and vacation:
     #   return True
    else:
        return False

print(sleep_in(True,False))