from tkinter import font


class Graphics:
    
    def __init__(self, canvas):
        self.__Canvas = canvas;
        self.__nowColor = "black";
        self.__nowLineColor = "black";
        self.__Canvas.place(x=0,y=0);
        self.__nowSharpId = [];
    
    # 塗りつぶす色を決める
    def setColor(self,color):
        self.__nowColor = color;
    
    def getColor(self):
        return self.__nowColor;
    
    # 外側のラインの色を決める
    def setLineColor(self,lineColor):
        self.__nowLineColor = lineColor;
    
    def getLineColor(self):
        return self.__nowLineColor;
    
    def setBothColor(self,color,lineColor):
        self.__nowColor = color;
        self.__nowLineColor = lineColor;

    def fillRect(self,x,y,width,hieght):
        self.__nowSharpId.append(self.__Canvas.create_rectangle(x, y, x+width, y+hieght, fill = self.getColor(), outline = self.getLineColor()));
        
    def fillOval(self,x,y,width,hieght):
        self.__nowSharpId.append(self.__Canvas.create_oval(x-int(width/2), y-int(hieght/2), width*2, hieght*2,fill = self.getColor(), outline = self.getLineColor()));
    
    def drawText(self ,x,y,string,size):
        self.__nowSharpId.append(self.__Canvas.create_text(x,y,text=string,font=("",size),fill = self.getColor()));
    
    def drawLine(self ,x1,y1,x2,y2):
        self.__nowSharpId.append(self.__Canvas.create_line(x1,y1,x2,y2,fill=self.getColor()));
        
    def drawImage(self,x,y,img):
        self.__nowSharpId.append(self.__Canvas.create_image(x,y,image=img));
        
    #描画のはじめに必ずこれを実行する
    def clear(self):
        
        count =0;
        
        if(len(self.__nowSharpId) > 0):
            for i in range(len(self.__nowSharpId)):
                if(len(self.__nowSharpId) > 0):
                    i-=count;
                    self.__Canvas.delete(self.__nowSharpId[i]);
                    self.__nowSharpId.pop(i);
                    count += 1;
                else:
                    break;
            
        
        