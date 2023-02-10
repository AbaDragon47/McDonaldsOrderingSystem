#Rocio's API reading class
import pandas
import csv
 
menu =[]
# reading the CSV file
with open('menu.csv') as menuData:
    m = csv.reader(menuData) 
    dataInf = next(menuData)
    #adding rows of each menu item (with nutritional info) to menu array
    for row in m: 
        menu.append(row)
 
def dataInfo():
    return dataInf

def allData():
    return menu

#checking
print(dataInfo())
print(allData())