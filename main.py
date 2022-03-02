import tkinter
import graphics
import gameMode as mode

# ウィンドウの生成
Root = tkinter.Tk();
# グラフィクスオブジェクトの生成
g_gra = graphics.Graphics(tkinter.Canvas(Root,width=600,height=500,bg="white"));

flg =  mode.GameMode.START; 

def gameLoop():
    
    #TODO:ゲームの処理を書く
    
    g_gra.fillRect(10,10,10,10);
    
    
    
    g_gra.clear();
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