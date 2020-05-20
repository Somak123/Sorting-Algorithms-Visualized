# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:23:14 2020

@author: SOMAK
"""

import time

def merge_sort(data,drawData,timetick):
    merge_sort_alg(data,0,len(data)-1,drawData,timetick)
    
    
    
def merge_sort_alg(data,left,right,drawData,timetick):
    if(left<right):
        mid=(left+right)//2
        merge_sort_alg(data,left,mid,drawData,timetick)
        merge_sort_alg(data,mid+1,right,drawData,timetick)
        merge(data,left,mid,right,drawData,timetick)
        
        
def merge(data,left,mid,right,drawData,timetick):
    
    drawData(data,getColorArray(len(data),left,mid,right))
    time.sleep(timetick)
    leftpart=data[left:mid+1]
    rightpart=data[mid+1:right+1]
    
    leftidx=rightidx=0
    dataidx=left
    while(leftidx<len(leftpart) and rightidx<len(rightpart)):
        if(leftpart[leftidx]<=rightpart[rightidx]):
            data[dataidx]=leftpart[leftidx]
            leftidx+=1
            dataidx+=1
        else:
            data[dataidx]=rightpart[rightidx]
            rightidx+=1
            dataidx+=1
            
            
    while(leftidx<len(leftpart)):
        data[dataidx]=leftpart[leftidx]
        leftidx+=1
        dataidx+=1
        
    while(rightidx<len(rightpart)):
        data[dataidx]=rightpart[rightidx]
        rightidx+=1
        dataidx+=1
    
    drawData(data,['green' if x>=left and x<=right else 'white' for x in range(len(data))])
    time.sleep(timetick)
            
def getColorArray(length,left,mid,right):
    colorArray=[]
    for i in range(length):
        if i>=left and i<=right:
            if i<=mid:
                colorArray.append('blue')
            else:
                colorArray.append('yellow')
        else:
            colorArray.append('white')
    return colorArray