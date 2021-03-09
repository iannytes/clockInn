import gspread
import datetime
gc = gspread.service_account(filename="sheets_auth.json")
sh = gc.open_by_key('17aL0l7sOI_S1Xdd9gG1xsYCU72PagJz5kG2qswIXtHw')
current_date = datetime.datetime.now()
# creates list of dates in program
datetimes = []
super_email = []
employee_names = []
hour_match = []
hours_sheet = sh.sheet1
#Check all dates in sheet and add them to list (date col is 4)
def make_list(col, list) :
    loop = 2
    for rows in hours_sheet.col_values(col):
        val = hours_sheet.cell(loop, col).value
        #makes sure you dont return a blank value to end of list
        try:   
            if len(val) > 0 :
            #make sure the list has no repeats.
                if val not in list :
                     list.append(val)
                     loop = loop + 1 
        except:
             print('exception')
             return False


def get_pay_period():
    start_date = datetime.datetime.strptime(min(datetimes), "%m/%d/%y")
    end_date = start_date + datetime.timedelta(days=14)
    print(start_date)
    print(end_date)
            

def get_hour(name,):
    loop = 0
    global hours_worked
    hours_worked = 0
    for rows in hours_sheet.col_values(2):
        loop = loop + 1 
        if name == hours_sheet.cell(loop, 1).value:
            hours_worked = int(hours_sheet.cell(loop, 2).value) + hours_worked

           
#creates list for super email names of employees and dates worked.        
make_list(4, datetimes)
make_list(1, employee_names)
make_list(6, super_email)
get_pay_period()
print(datetimes)
print(employee_names)
print(super_email)


for name in employee_names:
    get_hour(name)
    hour_match.append(hours_worked)

    

print(employee_names, hour_match)
            
        