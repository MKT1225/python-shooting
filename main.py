import tkinter
import graphics
import gameMode as mode

global g_gra;

flg =  mode.GameMode.START; 

def gameLoop(root):
    
    #TODO:ゲームの処理を書く
    
    #TODO:ループ条件をかく
    
    root.after(50,gameLoop);

#main関数です。
def main():
        
    # ウィンドウの生成
    Root = tkinter.Tk();
    Root.title("Shooting-python");
    
    #ウィンドウを真ん中に表示する処理
    Root.geometry("{}x{}+{}+{}".format(600,500,int(Root.winfo_screenwidth()/2-300),int(Root.winfo_screenheight()/2-250)));
    
    # グラフィクスオブジェクトの生成
    g_gra = graphics.Graphics(tkinter.Canvas(Root,width=600,height=500,bg="white"));
    
    g_gra.fillRect(10,30,100,100);
    
    # メインループの実行
    Root.mainloop();
    

if __name__ == "__main__" :
    main();