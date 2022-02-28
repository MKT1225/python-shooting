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

    def fillRect(self,x,y,wight,higth):
        self.__Canvas.create_rectangle(x, y, x+wight, y+higth, fill = self.getColor(),outline=self.getLineColor());  
        