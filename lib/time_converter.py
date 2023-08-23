#

def time_converter(hour, minute, TimeOfDay):
    if 0 <= minute < 60:
        if TimeOfDay == "pm" and hour != 12:
            hour += 12
        elif TimeOfDay == "am" and hour == 12:
            hour = 0

        #make the hr and min into strings
        hour_string = str(hour).zfill(2)
        minute_string = str(minute).zfill(2)

        #concatenates the hour and minute into a string + h 
        time_in_24hr = hour_string + minute_string + "h"
        return time_in_24hr 
    else:
        print("Please enter valid minute value")

#tests
print(time_converter(8, 30, "am")) #0830h
print(time_converter(12, 30, "am")) #0030h
print(time_converter(12, 00, "pm")) #1200h
print(time_converter(10, 3, "am")) #1003h
print(time_converter(8, 220, "pm")) #Please enter valid minute value

