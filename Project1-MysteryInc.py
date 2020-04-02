# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:43:34 2020

@authors: Cortney, Thuy, Shireen, Kazi
"""

'''employmentData = open("TotalPrivateEmployment-data.csv", "r") #data file and program are in same directory4
lineList = [line.rstrip('\n') for line in open("TotalPrivateEmployment-data.csv")]
'''
import csv
with open('TotalPrivateEmployment-data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(row)
        line_count += 1
    print(f'Processed {line_count} lines.')

President_file = open('Presidents.txt','r')
president=[]
party=[]
termServed=[]
totalDemocrats = 0
with open("Presidents.txt", "r") as President_file:
    csv_reader = csv.reader(President_file, delimiter=',')
    for line in csv_reader:
      print(line[1])
      president = line[0]
      party = line[1]
      termServed = line[2:]
      if party == 'Democrat':
          totalDemocrats += 1
      print(president, "is a ", party, ".")
      print("Years served are ", termServed)
      print(len(termServed), "years served.")
    print("There are", totalDemocrats, "total democrats.")
        

President_file.close()


csv_file.close()
