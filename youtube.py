import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('test.json', scope)

client = gspread.authorize(credentials)

wks = client.open('testSheet').sheet1

#print(wks.get_all_records())
print(wks.range)
#export data from csv file and put desc into the YouTube Videos

#commit only 3
#https://docs.google.com/spreadsheets/d/1A2C7qxAwT9xopYMWOqyUhBOHdIWRRHxak6-wmegAX_k/edit#gid=0
