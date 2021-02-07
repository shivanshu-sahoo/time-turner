from timeZone import UTC_offset
import datetime
def convertTime(userSentTime,userSentTimeZone,userReactedTimeZone,period):

    userSentOffset=UTC_offset(userSentTimeZone)
    userReactedOffset=UTC_offset(userReactedTimeZone)
    day=0
    if ":" not in userSentTime:
        userSentTime+= ":00"
        
    if ":" not in userSentOffset:
        userSentOffset+= ":00"

    if ":" not in userReactedOffset:
        userReactedOffset+= ":00"    

    userTime = userSentTime.split(":")
    userOffsetTime = userSentOffset.split(":")
    requiredOffsetTime= userReactedOffset.split(":")

    userTime= list(map(int,userTime))
    userOffsetTime= list(map(int,userOffsetTime))
    requiredOffsetTime= list(map(int,requiredOffsetTime))


    if(period=="pm"):
        userTime[0]+=12
        if userTime[0]==24:
            userTime[0]=12
    if(period=="am" and userTime[0]==12):
        userTime[0]=0
    
    user_time= datetime.datetime(2021, 2, 7, userTime[0],  userTime[1], 0)
    print(userTime)
    if(userOffsetTime[1]>0):
        utc_time=user_time-datetime.timedelta(hours=userOffsetTime[0],minutes=userOffsetTime[1])
    else:
        utc_time=user_time+datetime.timedelta(hours=abs(userOffsetTime[0]),minutes=abs(userOffsetTime[1]))
    


    if(requiredOffsetTime[1]>0):
        converted_time=utc_time+datetime.timedelta(hours=requiredOffsetTime[0],minutes=requiredOffsetTime[1])
    else:
        converted_time=utc_time-datetime.timedelta(hours=abs(requiredOffsetTime[0]),minutes=abs(requiredOffsetTime[1]))
    print(converted_time)

    converted_time_hour=int(converted_time.strftime("%H"))
    converted_time_minute=converted_time.strftime("%M")
    if(converted_time_hour>12):
        final_time_hour=converted_time_hour-12
        period='pm'
    elif converted_time_hour==0:
        final_time_hour=12
        period="am"
    elif converted_time_hour==12:
        final_time_hour=12
        period="pm"
    else:
        final_time_hour=converted_time_hour
        period="am"


    final_time= str(final_time_hour)+":"+converted_time_minute

    date=int(converted_time.strftime("%d"))
    if date==6:
        day="previous day"
    elif date==7:
        day="same day"
    else:
        day="next day"

    print(day)
    print(final_time)
    print(period)
    return final_time,period,day



