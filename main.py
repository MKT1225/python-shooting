import sys
import tkinter
import graphics
import gameMode as mode

# ウィンドウの生成
Root = tkinter.Tk();
# グラフィクスオブジェクトの生成
gra = graphics.Graphics(tkinter.Canvas(Root,width=600,height=500,bg="white"));

gameFlg =  mode.GameMode.START; 

images = [tkinter.PhotoImage(file="img\Quu.png"),];
#           key.A key.D Key.W Key.S Key.K Key.Enter
pushKeys = [False,False,False,False,False,False];

def keyPressed(event):
    
    pushKeyCode = event.keysym

    match(pushKeyCode):
        case "a":
            pushKeys[0]=True;
        case "d":
            pushKeys[1]=True;
        case "w":
            pushKeys[2]=True;
        case "s":
            pushKeys[3]=True;
        case "k":
            pushKeys[4]=True;
        case "Return":
            pushKeys[5]=True;
            
def keyReleased(event):
    
    pushKeyCode = event.keysym

    match(pushKeyCode):
        case "a":
            pushKeys[0]=False;
        case "d":
            pushKeys[1]=False;
        case "w":
            pushKeys[2]=False;
        case "s":
            pushKeys[3]=False;
        case "k":
            pushKeys[4]=False;
        case "Return":
            pushKeys[5]=False;
    
            
def gameLoop():
    
    global gameFlg;
    
    gra.clear();
    
    #TODO:ゲームの処理を書く
    match(gameFlg):
        
        case mode.GameMode.START:
            gra.drawText(300,150,"Shooting",100);
            gra.drawText(300,250,"Push Enter to Play",50);
            
            if(pushKeys[5]):
                gameFlg=mode.GameMode.GAME;
                
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
    
    Root.bind("<KeyPress>", keyPressed);
    Root.bind("<KeyRelease>", keyReleased)
    
    sys.setrecursionlimit(2000);

    Root.after(50,gameLoop());
    
    # メインループの実行
    Root.mainloop();
    

if __name__ == "__main__" :
    main();