import pandas as pd

data = pd.read_csv('test.csv', delimiter = ',',
                   names = ['link','topic','chap','subject','class','hin','mb','title','tags','prev','next'])
x = data.link[3]
print(x)
# import csv
# filename = 'test.csv'

# print(filename[6])












# with open(filename, 'r') as csvfile:
#     csvreader = csv.reader(csvfile)

#     fields = csvreader.next()

#     for rows in csvreader:
#         rows.append(row)

#     print("Total no. of rows: %d"%(csvreader.line_num))    

#commit only 3
#1 - https://docs.google.com/spreadsheets/d/1A2C7qxAwT9xopYMWOqyUhBOHdIWRRHxak6-wmegAX_k/edit#gid=0
#2 - https://docs.google.com/spreadsheet/ccc?key=0ArM5yzzCw9IZdEdLWlpHT1FCcUpYQ2RjWmZYWmNwbXc&output=csv

# --- import the csv file to python -- make upload file option on the page
# --- use pandas aas pd to scale
# --- rearrange the data into TITLE, DESC... parts
# --- 
