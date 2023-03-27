import datetime
from pathlib import Path

dateraw = datetime.date.today()
date = str(dateraw.year) + '-' + str(dateraw.month) + '-' + str(dateraw.day)

def ParseDate(folder):
    returndate = []
    with open(folder, "r") as file:
        for line in file:
            dateold = line
        for date in dateold.split('-'):
            returndate.append(int(date))
    return returndate
        
def DiffDays(dateold, datenow):
    dateold = datetime.date(dateold[0], dateold[1], dateold[2])
    diff = datenow - dateold
    return diff.days
    
def CreateDate(folder):
    with open(folder, "w") as file:
        file.write(date)

def CheckDate(folder, daysforcheck):
    if Path(folder).is_file():
        dateold = ParseDate(folder)
        diff = DiffDays(dateold, dateraw)
        if diff >= daysforcheck:
            returnvalue = True
        else:
            returnvalue = False
    else:
        returnvalue = True
    return returnvalue