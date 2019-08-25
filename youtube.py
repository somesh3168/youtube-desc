import pandas as pd

data = pd.read_csv('test.csv', delimiter = ',',
                   names = ['link','topic','chap','subject','clas','hin','mb','title','tags','prev','next'])
print("Enter Youtube Link")
input_link = input()
x = len(data.link)

for i in range(1, x):
    if input_link == data.link[i]:
        print('Index no.',i)
        print(data.title[i])
        print('Desc\n')
        desc = str(data.subject[i]) + '\n'+ str(data.chap[i])+ '\n'+ str(data.hin[i])+ '\n'+ str(data.mb[i])+ '\n'+ str(data.tags[i])+ '\n'+ str(data.prev[i])+ '\n'+ str(data.next[i])
        print(desc)



#1 - https://docs.google.com/spreadsheets/d/1A2C7qxAwT9xopYMWOqyUhBOHdIWRRHxak6-wmegAX_k/edit#gid=0
#2 - https://docs.google.com/spreadsheet/ccc?key=0ArM5yzzCw9IZdEdLWlpHT1FCcUpYQ2RjWmZYWmNwbXc&output=csv

