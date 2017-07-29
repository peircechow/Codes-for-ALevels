
def padding(): #pad left or right
    binNumber = 10010
    print('{}'.format(str(binNumber)).rjust(8,'0'))
    # "00010010"

def validateDate():
    import datetime
    correctDate = None
    try:
        newDate = datetime.datetime(2008,11,42) #YYYY,MM,DD
        correctDate = True
    except ValueError:
        correctDate = False
    print(str(correctDate))

def diffDates(): # takes the difference of dates
    import datetime as d
    d1 = d.datetime(2017,1,20) # year month day
    d2 = d.datetime(2000,1,30) 
    print((d1-d2).days) # d.timedelta(days)

def XDaysAfter():
    import datetime as d
    d1 = d.datetime(2017,1,20)
    daysAfter = 90
    print("{} after {} is {}".format(daysAfter, d1, d1+d.timedelta(daysAfter))
          
def timeInterval():
    # https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings 
    from datetime import datetime
    s1 = '10:33:26' 
    s2 = '11:15:49' # for example
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
