import gspread
from pprint import PrettyPrinter as pprint


gc = gspread.service_account(filename='sheets_auth.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/17aL0l7sOI_S1Xdd9gG1xsYCU72PagJz5kG2qswIXtHw')

hours_sheet = sh.sheet1


#Check to see if new hours have been added.


#Check to see what billable week is by pulling date in a block of 2 weeks.

#Email supervisors that have to verify hours worked with details entered by user


