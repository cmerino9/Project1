# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:43:34 2020

@authors: Cortney, Thuy, Shireen, Kazi
"""
import csv
with open('TotalPrivateEmployment-data.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for line in csv_reader:
        year = line[0]
        totalJobs = 0

President_file = open('Presidents.txt','r')
president = []
party = []
termServed = []
totalDemocrats = 0
with open("Presidents.txt", "r") as President_file:
    csv_reader = csv.reader(President_file, delimiter=',')
    for line in csv_reader:
      president = line[0]
      party = line[1]
      termServed = line[2:]
      if party == 'Democrat':
          totalDemocrats += 1
          
      print(president, "is a", party, "and served", len(termServed), "years.")
      print("Years served are", termServed)
    print("There are", totalDemocrats, "total democrats.")
        
csv_file.close()
President_file.close()
               


