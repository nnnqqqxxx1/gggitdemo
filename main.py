from tkinter import *
import numpy
import scipy
import math
t=Tk()
t.title('最短路径')
t.geometry('1600x900')
Label(t,text='点的个数').place(x=5,y=5)#输入点的个数
x1=''
global e1
e1=Entry(t,width=10)
e1.place(x=60,y=5)
Label(t,text='       到               的距离:').place(x=22,y=40)
dis=Entry(t,width=5)
dis.place(x=185,y=40)
start=Entry(t,width=5)
start.place(x=5,y=40)
end=Entry(t,width=5)
end.place(x=75,y=40)
a=0#变量a用来判断按钮回调函数是否会被触发