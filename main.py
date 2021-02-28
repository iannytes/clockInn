import gspread
from pprint import PrettyPrinter as pprint
import datetime


gc = gspread.service_account(filename="sheets_auth.json")
sh = gc.open_by_key('17aL0l7sOI_S1Xdd9gG1xsYCU72PagJz5kG2qswIXtHw')
current_date = datetime.datetime.now()


hours_sheet = sh.sheet1
values = hours_sheet.row_values(2)

#Check to see if new hours have been added.
print(values)


#Check to see what billable week is by pulling date in a block of 2 weeks.

#Email supervisors that have to verify hours worked with details entered by user


