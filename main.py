import gspread
from pprint import PrettyPrinter as pprint
import datetime

from pyasn1.type.univ import Null


gc = gspread.service_account(filename="sheets_auth.json")
sh = gc.open_by_key('17aL0l7sOI_S1Xdd9gG1xsYCU72PagJz5kG2qswIXtHw')
current_date = datetime.datetime.now()

# creates list of dates in program
datetimes = []

#finds earliesy date in list

#variable for 2 week pay period interval
pay_period_delta = datetime.timedelta(days=14)


hours_sheet = sh.sheet1
values = hours_sheet.row_values(2)


#Check all dates in sheet and add them to list (date col is 4)
def add_dates(col) :
    loop = 1
    for rows in hours_sheet.col_values(col):
        loop = loop + 1 
        val = hours_sheet.cell(loop, col).value
        
        #makes sure you dont return a blank value to end of list
        if len(val) > 0:
           
            val = hours_sheet.cell(loop, col).value
            datetimes.append(val)
            print (len(val))
            print (rows)

add_dates(4)

print(datetimes)

#Check to see what billable week is by pulling date in a block of 2 weeks.

#Email supervisors that have to verify hours worked with details entered by user


