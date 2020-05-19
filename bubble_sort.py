# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:50:02 2020

@author: SOMAK
"""

import time

def bubble_sort(data,drawData,timetick):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if(data[j]>data[j+1]):
                t=data[j]
                data[j]=data[j+1]
                data[j+1]=t
                drawData(data,['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
                time.sleep(timetick)
    drawData(data,['green' for x in range(len(data))])