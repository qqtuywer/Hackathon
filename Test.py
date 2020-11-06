# coding=utf-8
import json
import requests
import time
import sys
import os


time_start = time.time()
if __name__ == '__main__':
    get_time = time.strftime('%Y-%m-%d %H:%M:%S')
    link = r'C:\Users\WZN3SZH\Desktop\Hackathon'
    point_line1=[0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,
                 0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,
                 0,0,0,0,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,
                 0,0,0,0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
    point_bar2=[10,11,11,12]
    
    #请求folder link
    folder_link = {'folder_link': link}
    response = requests.post('http://10.178.62.36:50001/test_upload_video', json=folder_link)

    print(response.text)
    while(1) :
        #请求first frame的坐标
        first_frame = {'first_frame': link}
        response = requests.post('http://10.178.62.36:50001/test_line_bar_data', json=first_frame)
        #time stamp  
        print(time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())))
        print(response.text)
        time.sleep(1)

    time_end = time.time()
    print('totally cost', time_end - time_start)