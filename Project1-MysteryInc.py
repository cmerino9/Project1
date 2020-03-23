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
parties=[]
for line in President_file:
    tmp_list = line.split("\n")
    president = tmp_list[0]
    parties = tmp_list[1:]
    Slice=tmp_list[2:]
    for each in Slice:
        tmp_list.append(each)
    print(tmp_list)
        
President_file.close()


csv_file.close()
