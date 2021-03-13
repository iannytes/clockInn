import gspread
import datetime
import os
import smtplib

gc = gspread.service_account(filename="sheets_auth.json")
sh = gc.open_by_key('17aL0l7sOI_S1Xdd9gG1xsYCU72PagJz5kG2qswIXtHw')
current_date = datetime.datetime.now()
# creates lists of data in program 
datetimes = [] #days that have been worked
super_email = [] #supervisor emails
employee_names = [] #names of Employess
hour_match = [] #How many hours thos employees have worked


hours_sheet = sh.sheet1
#Check data in sheet and make a list from it.
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

#gets two weeks from the earliest submitted date of work
def get_pay_period():
    global start_date
    global end_date
    start_date = datetime.datetime.strptime(min(datetimes), "%m/%d/%y")
    end_date = start_date + datetime.timedelta(days=14)
    print(start_date)
    print(end_date)
            
#calculates hours worked for a given name in the list
def get_hour(name):
    loop = 0
    global hours_worked
    hours_worked = 0
    for rows in hours_sheet.col_values(2):
        loop = loop + 1 
        if name == hours_sheet.cell(loop, 1).value:
            hours_worked = int(hours_sheet.cell(loop, 2).value) + hours_worked

def email_alert(loop):
    recipient = str(super_email[loop])
    subject = 'Verifying Hours Worked'
    msg = 'Hello, I am a bot, I am contacting you to verify ' + str(employee_names[loop] + ' worked a total of *' + str(hour_match[loop]) + '* hours between' + str(start_date) + ' and ' + str(end_date))
    print(recipient)
    print(subject)
    print(msg)
    send_email_alert('ian@medyxhealth.com', subject, msg)


def send_email_alert(recipient, subject, msg):
    
    #sets up access to mailserver base on the user info located in .zshrc or whatever the defaul shell is
    email_username = os.environ.get('email_username')
    email_password = os.environ.get('email_python_password')
    
    server = smtplib.SMTP('smtp.gmail.com')
    server.connect('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.login(email_username, email_password)
  
    #  formats the email to be sent properly by .sendmail
    email = f'Subject: {subject}\n\n{msg}'

    server.sendmail(email_username, recipient, email)


           
#creates list for super email, names of employees, and dates worked.        
make_list(4, datetimes)
make_list(1, employee_names)
make_list(6, super_email)
get_pay_period()
print(datetimes)
print(employee_names)
print(super_email)

#matches hours to names
for name in employee_names:
    get_hour(name)
    hour_match.append(hours_worked)

print(hour_match)
loop = 0

for name in employee_names:
    permission_to_email = input('Would you like to submit *' + str(hour_match[loop]) + '* hours worked for ' + str(employee_names[loop]) + '? [y/n]')

    if permission_to_email.upper() == 'Y' :
            email_alert(loop)
            print('calling loop')
            loop = loop + 1 
    else :
            permission_to_email = 'null'
            loop = loop + 1


            
        