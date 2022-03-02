import tkinter
import graphics
import gameMode as mode

# ウィンドウの生成
Root = tkinter.Tk();
# グラフィクスオブジェクトの生成
gra = graphics.Graphics(tkinter.Canvas(Root,width=600,height=500,bg="white"));

flg =  mode.GameMode.START; 

images = [tkinter.PhotoImage(file="img\Quu.png"),];


def gameLoop():
    
    #TODO:ゲームの処理を書く
    gra.drawImage(100,100,images[0]);
    
    
    gra.clear();
    
    #TODO:ループ条件をかく
    
    

#main関数です。
def main():
    
        
    Root.title("Shooting-python");
    
    #ウィンドウを真ん中に表示する処理
    Root.geometry("{}x{}+{}+{}".format(600,500,int(Root.winfo_screenwidth()/2-300),int(Root.winfo_screenheight()/2-250)));
    
    

    Root.after(50,gameLoop());
    
    # メインループの実行
    Root.mainloop();
    

if __name__ == "__main__" :
    main();