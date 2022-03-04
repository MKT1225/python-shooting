import sys
import tkinter
from turtle import goto
import graphics
import gameMode as mode

# ウィンドウの生成
Root = tkinter.Tk();
# グラフィクスオブジェクトの生成
gra = graphics.Graphics(tkinter.Canvas(Root,width=600,height=500,bg="white"));

gameFlg =  mode.GameMode.START; 

images = [tkinter.PhotoImage(file="img\Quu.png"),];


def gameLoop():
    
    gra.clear();
    
    #TODO:ゲームの処理を書く
    match(gameFlg):
    
        case mode.GameMode.START:
            gra.fillOval(100,100,100,100);
            gra.drawText(100,200,"test",30);
            gra.fillRect(0,0,300,10);
        case mode.GameMode.GAME:
            print();
        case mode.GameMode.BOSS:
            print();
        case mode.GameMode.GAMEOVER:
            print();
        case mode.GameMode.CLEAR:
            print();
        case __:
            print("ERROR");

    #TODO:ループ条件をかく
    
    Root.after(50,gameLoop);
  

#main関数です。
def main():
    
        
    Root.title("Shooting-python");
    
    #ウィンドウを真ん中に表示する処理
    Root.geometry("{}x{}+{}+{}".format(600,500,int(Root.winfo_screenwidth()/2-300),int(Root.winfo_screenheight()/2-250)));
    
    sys.setrecursionlimit(2000);

    Root.after(50,gameLoop());
    
    # メインループの実行
    Root.mainloop();
    

if __name__ == "__main__" :
    main();