def conversion_from_seconds(second):
    hours=second//3600
    minutes=(second-(hours*3600))//60
    seconds=(second-(hours*3600)-(minutes*60))
    return (hours,minutes,seconds)
    
hours,minutes,seconds = conversion_from_seconds(10000)
print(hours,minutes,seconds)
