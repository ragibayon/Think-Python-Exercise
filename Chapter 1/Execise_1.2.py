# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:59:42 2020
Exercise 1.2 
@author: Ragib Shahariar Ayon
"""
#%% Count seconds!
def seconds_count(hours=0, minutes=0, seconds=0):
    result=((minutes+(hours*60))*60)+seconds
    print("{}:{}:{} has {} seconds".format(hours,minutes,seconds,result))
    return result

#seconds_count(int(input("Input hours: ")),int(input("Input minutes: ")),int(input("Input seconds: ")))

#%% KM to Mile Conversion

def miles_count(KM=0):
    miles=KM/1.61
    print("{} Kilometers has {} miles".format(KM,miles))
    return miles

#miles_count(int(input("How many kilometers did you ran? ")))
#%%
def pace(distance=0, hour=0, minutes=0, seconds =0):
    
    mps=miles_count(distance)/seconds_count(hour, minutes,seconds)
    mpm=mps*60
    mph= mpm*60
    return print("Your average pace is {} MPH {} MPM {} MPS".format(mph,mpm,mps))

pace(int(input("Your distance: ")),int(input("Hours: ")),int(input("Minutes: ")),int(input("Seconds: ")))
