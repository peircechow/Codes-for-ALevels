
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
