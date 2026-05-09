import yagmail
import os
import glob

receiver = "mygmail@gmail.com"  # receiver email address
body = "Attendance File"  # email body

# Find the latest attendance file
list_of_files = glob.glob('Attendance' + os.sep + '*.csv')
if not list_of_files:
    print("No attendance files found in the Attendance directory.")
    exit()

latest_file = max(list_of_files, key=os.path.getctime)
filename = latest_file

# Note: You need to update these with your real email and password/app password
yag = yagmail.SMTP("mymail@gmail.com", "my_password")

try:
    yag.send(
        to=receiver,
        subject="Attendance Report", 
        contents=body, 
        attachments=filename, 
    )
    print("Email Sent Successfully")
except Exception as e:
    print(f"Error sending email: {e}")

