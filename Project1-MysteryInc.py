# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:43:34 2020

@authors: Cortney, Thuy, Shireen, Kazi
"""

employmentData = open("TotalPrivateEmployment-data.csv", "r") #data file and program are in same directory
for aline in employmentData:
    values = aline.split() #we need to figure out where to split this data
    print(values)
    
employmentData.close()