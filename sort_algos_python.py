# -*- coding: utf-8 -*-
"""
Created on Mon May 18 01:23:49 2020

@author: SOMAK
"""

from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
root=Tk()
root.title('Sorting Algorithms Visualized')
root.maxsize(900,600)
root.config(bg='black')

#variables
selected_alg=StringVar()
data=[]


def drawData(data,colorArray):
    canvas.delete('all')
    c_height=380
    c_width=600
    x_width=c_width/(len(data)+1)
    offset=30
    spacing=10
    normalizedData=[i/max(data) for i in data]
    for i,height in enumerate(normalizedData):
        #topleft
        x0=i*x_width+offset+spacing
        y0=c_height-height*340
        #bottomright
        x1=(i+1)*x_width+offset
        y1=c_height
        
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    root.update_idletasks()


def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
         data.append(random.randrange(minVal, maxVal+1))

    drawData(data,['red' for x in range(len(data))])

def startAlgo():
    global data
    #if not data:
     #   return
    if algMenu.get()=='Bubble Sort':
        bubble_sort(data,drawData,speedScale.get())
        drawData(data,['green' for x in range(len(data))])
    elif algMenu.get()=='Merge Sort':
        merge_sort(data,drawData,speedScale.get())
        drawData(data,['green' for x in range(len(data))])
    elif algMenu.get()=='Quick Sort':
        quick_sort(data,0,len(data)-1,drawData,speedScale.get())
        drawData(data,['green' for x in range(len(data))])
    #bubble_sort(data,drawData,speedScale.get())
        
    
        
    
#base_layout
UI_Frame=Frame(root,width=600,height=200,bg='grey')
UI_Frame.grid(row=0,column=0,padx=10,pady=5)
canvas=Canvas(root,width=600,height=300,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

#UIArea
Label(UI_Frame,text='Algorithm: ',bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu=ttk.Combobox(UI_Frame,textvariable=selected_alg,values=['Bubble Sort','Quick Sort','Merge Sort'])
algMenu.grid(row=0,column=1,padx=5,pady=5)
algMenu.current(0)
speedScale=Scale(UI_Frame,from_=0.1,to=2.0,length=200,digits=2,resolution=0.2,orient='horizontal',label='Select Speed[s]')
speedScale.grid(row=0,column=2,padx=5,pady=5)
Button(UI_Frame,text='Start',command=startAlgo,bg='red').grid(row=0,column=3,padx=5,pady=5)


#row[1]

sizeEntry=Scale(UI_Frame,from_=3,to=25,resolution=1,orient='horizontal',label='Data Size')
sizeEntry.grid(row=1,column=0,padx=5,pady=5)


minEntry=Scale(UI_Frame,from_=0,to=10,resolution=1,orient='horizontal',label='Min Value')
minEntry.grid(row=1,column=1,padx=5,pady=5)


maxEntry=Scale(UI_Frame,from_=10,to=100,resolution=1,orient='horizontal',label='Max Value')
maxEntry.grid(row=1,column=2,padx=5,pady=5)



Button(UI_Frame,text='Generate',command=Generate,bg='white').grid(row=1,column=3,padx=5,pady=5)

root.mainloop()