import gspread
import datetime




gc = gspread.service_account(filename="sheets_auth.json")
sh = gc.open_by_key('17aL0l7sOI_S1Xdd9gG1xsYCU72PagJz5kG2qswIXtHw')
current_date = datetime.datetime.now()


worked_hours = {

}

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
                    list[val] = hours_sheet.cell(loop, 2).value

                    loop = loop + 1
                elif:
                    for names in worked_hours:
                        if val == names
                            worked_hours[val] = worked_hours[val] + hours_sheet.cell(loop, 2).value


        except:
            return False

 
            return False

make_list(1, worked_hours)
print(worked_hours)