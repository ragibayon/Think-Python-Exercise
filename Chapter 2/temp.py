# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:31:39 2020

@author: Ragib Shahariar Ayon
"""


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

