#HoursMinutesSeconds
#Convert seconds into a string for hours, minutes, and seconds. Test with assert statements

def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds==0:
        return '0s'

    hours=0
    minutes=0

    if totalSeconds>= 3600:
        hours = totalSeconds//3600 #divided //
        totalSeconds = totalSeconds % 3600 #remainder %
    else:
        hours=0

    if totalSeconds>= 60:
        minutes = totalSeconds//60
        totalSeconds = totalSeconds % 60
 
    seconds= totalSeconds 

    #Create a list and add suffixes (h,m,s) for readability
    hms=[] #establishing array to fill
    if hours>0:
        hms.append(str(hours)+ 'h')
    if minutes>0:
        hms.append(str(minutes)+ 'm')
    if seconds>0:
        hms.append(str(seconds)+ 's')

    return ' '.join(hms)