# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:07:26 2020

@author: SOMAK
"""
import time


def partition(data,head,tail,drawData,timetick):
    border=head
    pivot=data[tail]
    drawData(data,getColorArray(len(data),head,tail,border,border))
    time.sleep(timetick)
    
    for j in range(head,tail):
        if(data[j]<pivot):
            drawData(data,getColorArray(len(data),head,tail,border,j,True))
            time.sleep(timetick)
            data[border],data[j]=data[j],data[border]
            border+=1
        drawData(data,getColorArray(len(data),head,tail,border,j))
        time.sleep(timetick)
    drawData(data,getColorArray(len(data),head,tail,border,tail,True))
    time.sleep(timetick)
    data[border],data[tail]=data[tail],data[border]
    return border


def quick_sort(data,head,tail,drawData,timetick):
    if head<tail:
        index=partition(data,head,tail,drawData,timetick)
        quick_sort(data,head,index-1,drawData,timetick)
        quick_sort(data,index+1,tail,drawData,timetick)
        

def getColorArray(datalen,head,tail,border,curridx,isSwapping=False):
    color=[]
    for i in range(datalen):
        if i>=head and i<=tail:
            color.append('gray')
        else:
            color.append('white')
        
        if i==tail:
            color[i]='blue'
        elif i==border:
            color[i]='red'
        elif i==curridx:
            color[i]='yellow'
        
        if isSwapping:
            if i==border or i==curridx:
                color[i]='green'
    return color