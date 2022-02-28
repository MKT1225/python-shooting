import tkinter;
import graphics;

global g_nowSetColor;


#main関数です。
def main():
    
    g_nowSetColor = "green"
    
    Root = tkinter.Tk();
    Root.title("MIKOTO");
    Root.geometry("400x300");
    
    gra = graphics.Graphics(tkinter.Canvas(Root,width=400,height=300));
    
    gra.fillRect(100,100,50,50);
    
    
    Root.mainloop();
    



if __name__ == "__main__" :
    main();