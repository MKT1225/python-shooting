from msilib.schema import Font
from re import X
from textwrap import fill
from tkinter import font


class Graphics:
    
    def __init__(self, canvas):
        self.__Canvas = canvas;
        self.__nowColor = "black";
        self.__nowLineColor = "black";
        self.__Canvas.place(x=0,y=0);
    
    def setColor(self,color):
        self.__nowColor = color;
    
    def getColor(self):
        return self.__nowColor;
    
    def setLineColor(self,lineColor):
        self.__nowLineColor = lineColor;
    
    def getLineColor(self):
        return self.__nowLineColor;
    
    def setBothColor(self,color,lineColor):
        self.__nowColor = color;
        self.__nowLineColor = lineColor;

    def fillRect(self,x,y,width,hieght):
        self.__Canvas.create_rectangle(x, y, x+width, y+hieght, fill = self.getColor(), outline = self.getLineColor());
        
    def fillOval(self,x,y,width,hieght):
        self.__Canvas.create_oval(x, y, x+width, y+hieght,fill = self.getColor(), outline = self.getLineColor());
    
    def drawText(self ,x,y,string,size):
        self.__Canvas.create_text(x,y,text=string,font=("",size),fill = self.getColor());
        
    