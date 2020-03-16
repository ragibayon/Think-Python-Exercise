# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:43:31 2020
Exercise 2.2 Python interpreter as a calculator
@author: Ragib Shahariar Ayon
"""
import math
def volume_sphere(radius=0):
    volume= (4/3)*math.pi*(radius**3)
    print("The volume of the sphere is: {}".format(volume))
    return volume

volume_sphere(int(input("What is the radius of the sphere: ")))

#%%

def wholesale_cost(item_count=0,cover_price=0,bookstore_discount=0,shipping_cost=0):
    if item_count==1:
        shipping_cost=3
    else:
        shipping_cost=shipping_cost+(.75*(item_count-1))
    cost=(cover_price*item_count*(1-bookstore_discount/100))+shipping_cost
    
    print("Total whole sale cost is {}$".format(cost))
    return cost

wholesale_cost(int(input("Number of item: ")),float(input("Cover Price of the book: ")),int(input("Book Store discount: ")),int(input("Shipping cost: ")))
#%%
def end_time(start_time="6:52:0",easy_count=1,easy_pace="8:15",tempo_count=1,tempo_pace='7:12'):
    start_time_hour,start_time_min,start_time_sec=start_time.split(":")    
    easy_min,easy_sec=easy_pace.split(":")    
    tempo_min,tempo_sec=tempo_pace.split(':')    
    
    total_time_sec=((int(easy_min)*60+int(easy_sec))*easy_count)+((int(tempo_min)*60+int(tempo_sec))*tempo_count)+(int(start_time_min)*60)    
    
    total_time_min=total_time_sec//60
    additional_hour=total_time_min//60
    remaining_min=total_time_min%60
    remaining_sec=total_time_sec%60
    
    end_time="{}:".format(int(start_time_hour)+additional_hour)+"{}:".format(remaining_min)+"{}".format(remaining_sec)
    print("Start time={} \nEnd time:{}".format(start_time,end_time))
    return None

end_time()

