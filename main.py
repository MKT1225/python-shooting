import sys
import random;
import tkinter
import graphics
import gameMode as mode
import classes as cl;

# ウィンドウの生成
Root = tkinter.Tk();
# グラフィクスオブジェクトの生成
gra = graphics.Graphics(tkinter.Canvas(Root,width=600,height=500,bg="white"));

gameFlg =  mode.GameMode.START; 

player = cl.Player(20,20,10);

enemys = [];

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
        
        case "e":
            pushKeys[1] = True;
            pushKeys[2] = True;
            
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
        
        case "e":
            pushKeys[1] = False;
            pushKeys[2] = False;

def playerAction():
    
    global player;
    
    if player.reloadTime>0:
        player.reloadTime -=1;
    
    if pushKeys[0] and player.x >0:
        player.x -= player.moveSpeed;
    if pushKeys[1] and player.x <590:
        player.x += player.moveSpeed;
    if pushKeys[2] and player.y >0:
        player.y -= player.moveSpeed;
    if pushKeys[3] and player.y <490:
        player.y += player.moveSpeed;
    if pushKeys[4] and player.reloadTime == 0:
        player.addBullet();
        player.reloadTime = 5;
    if pushKeys[4] and pushKeys[5]:
        player.moveSpeed += 1;
        
def drawBullet():
    
    global gra;
    
    gra.setBothColor("blue","blue");
    
    for i in range(len(player.bullets)):
        gra.fillOval(player.bullets[i].x,player.bullets[i].y,radiusw = 3,radiush = 3);
    
    gra.setBothColor("red","red");
    
    for i in range(len(enemys)):
        for j in range(len(enemys[i].bullets)):
            gra.fillOval(enemys[i].bullets[j].x,enemys[i].bullets[j].y,radiusw = 3,radiush = 3);
        
    
            
def gameLoop():
    
    global gameFlg;
    global enemys;
    global player;
    
    gra.clear();
    
    #TODO:ゲームの処理を書く
    
    match(gameFlg):
        
        case mode.GameMode.START:
            gra.drawText(300,150,"Shooting",100);
            gra.drawText(300,250,"Push Enter to Play",50); 
            if(pushKeys[5]):
                gameFlg=mode.GameMode.GAME;
                
        case mode.GameMode.GAME:
            print(len(enemys));
            playerAction();
            gra.setBothColor("blue","cyan")
            gra.fillRect(player.x,player.y,10,10);
            
            if len(enemys)<8 :
                enemys.append(cl.Enemy(random.randint(550,600),random.randint(5,490),5));
            
            
            count =0;
            for i in range(len(enemys)):
                
                i -= count;
                
                gra.setBothColor("red","pink");
                gra.fillRect(enemys[i].x,enemys[i].y,10,10);
                enemys[i].move();
                enemys[i].moveBullet();
        
                if enemys[i].checkHit(player):
                    gameFlg = mode.GameMode.GAMEOVER;
                    enemys = [];
                    break;
                if enemys[i].checkHitBullet(player):
                    gameFlg = mode.GameMode.GAMEOVER;
                    enemys=[];
                    break;
                if player.checkHitBullet(enemys[i]):
                    enemys.pop(i);
                    count += 1;
                elif enemys[i].checkIsOut():
                    enemys.pop(i);
                    count += 1;
                    
                    
            player.moveBullet();
            drawBullet();
            
            
        case mode.GameMode.BOSS:
            print();
        case mode.GameMode.GAMEOVER:
            gra.setColor("red");
            gra.drawText(300,150,"GameOver",100);
            gra.setColor("black");
            gra.drawText(300,250,"Push Enter to Play again",40); 
            if(pushKeys[5]):
                gameFlg=mode.GameMode.START;
                player = cl.Player(20,20,10)
        case mode.GameMode.CLEAR:
            print();
        case __:
            print("ERROR");
   
    Root.after(50,gameLoop);
  

#main関数です。
def main():
    
        
    Root.title("Shooting-python");
    
    #ウィンドウを真ん中に表示する処理
    Root.geometry("{}x{}+{}+{}".format(600,500,int(Root.winfo_screenwidth()/2-300),int(Root.winfo_screenheight()/2-250)));
    
    Root.bind("<KeyPress>", keyPressed);
    Root.bind("<KeyRelease>", keyReleased)
    
    Root.resizable(False,False);
    
    sys.setrecursionlimit(2000);

    Root.after(50,gameLoop());
    
    # メインループの実行
    Root.mainloop();
    

if __name__ == "__main__" :
    main();