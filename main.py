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
def get():#储存按钮的回调函数
    global a
    if a!=0:#a不等于0时储存函数被触发
        if start.get().isdigit()==True and end.get().isdigit()==True and dis.get().isdigit()==True:
            a=2
            line=int(start.get())#起点
            column=int(end.get())#终点
            distance=int(dis.get())#距离
            pi=math.pi
            if column!=line and 0<column<=x1 and 0<line<=x1:#看一下两点是否符合条件
                if matrix[line-1][column-1]!=0:#如果已经生成过距离，需要重新定义
                    c.create_text(500+150*(math.cos(2*pi*(line-1)/x1)+math.cos(2*pi*(column-1)/x1)),375+150*(math.sin(2*pi*(line-1)/x1)+math.sin(2*pi*(column-1)/x1)),text=int(matrix[line-1][column-1]),fill='white')
                    #生成了一个白色的数字来覆盖掉原来的数字（距离）
                matrix[line-1][column-1]=distance#进行存储
                matrix[column-1][line-1]=distance#注意距离的无方向性
                trans[line-1][column-1]=column#暂时将终点定义为中间点
                trans[column-1][line-1]=line#另一边得倒过来
                c.create_text(500+150*(math.cos(2*pi*(line-1)/x1)+math.cos(2*pi*(column-1)/x1)),375+150*(math.sin(2*pi*(line-1)/x1)+math.sin(2*pi*(column-1)/x1)),text=int(distance))
                c.create_line(500+300*math.cos(2*pi*(line-1)/x1),375+300*math.sin(2*pi*(line-1)/x1),500+300*math.cos(2*pi*(column-1)/x1),375+300*math.sin(2*pi*(column-1)/x1),fill='red')
                #以上两行生成了红线和对应的距离
                if distance==0:#如果输错距离（两点之间本没有距离），则把生成的线和数字去掉（用白色的线条和数字去覆盖）
                    c.create_text(500+150*(math.cos(2*pi*(line-1)/x1)+math.cos(2*pi*(column-1)/x1)),375+150*(math.sin(2*pi*(line-1)/x1)+math.sin(2*pi*(column-1)/x1)),text=int(distance),fill='white')
                    c.create_line(500+300*math.cos(2*pi*(line-1)/x1),375+300*math.sin(2*pi*(line-1)/x1),500+300*math.cos(2*pi*(column-1)/x1),375+300*math.sin(2*pi*(column-1)/x1),fill='white')
            else:#如果你输入的点不存在或输入了两个一样的点，就会报错
                A=Tk()
                A.title('Error')
                A.geometry('200x100')
                Label(A,text='你输入的数据有误！',bg='red').place(x=50,y=20)