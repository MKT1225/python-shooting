
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

player = cl.Player(20,20);

enemys = [];

images = [tkinter.PhotoImage(file="img\Quu.png"),];
#           key.A key.D Key.W Key.S Key.K Key.Enter
pushKeys = [False,False,False,False,False,False];

orbs = [];

gameScore = 0;

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
        case "o":
            player.level += 1;
        

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
        
def drawBullet():
    
    global gra;
    
    gra.setColor("blue");
    
    for i in range(len(player.bullets)):
        gra.fillOval(player.bullets[i].x,player.bullets[i].y,radiusw = 3,radiush = 3);
    
    for i in range(len(player.barrageBullet)):
        gra.fillOval(player.barrageBullet[i].x,player.barrageBullet[i].y,radiusw = 3,radiush = 3);
    
    for i in range(len(enemys)):
        gra.setColor(enemys[i].color);
        for j in range(len(enemys[i].bullets)):
            gra.fillOval(enemys[i].bullets[j].x,enemys[i].bullets[j].y,radiusw = enemys[i].size//3,radiush = enemys[i].size//3);
            
def drawOrb():
    
    global gra;
    
    gra.setColor("yellow");
    
    for i in range(len(orbs)):
        gra.fillOval(orbs[i].x,orbs[i].y,4,4);
        
    
            
def gameLoop():
    
    global gameFlg;
    global enemys;
    global player;
    global gameScore;
    global orbs;
    
    gra.clear();
    
    #TODO:ゲームの処理を書く
    
    match(gameFlg):
        
        case mode.GameMode.START:
            gra.drawText(300,150,"Shooting",100);
            gra.drawText(300,250,"Push Enter to Play",50); 
            if(pushKeys[5]):
                gameFlg=mode.GameMode.GAME;
                
        case mode.GameMode.GAME:

            playerAction();
            gra.setBothColor(player.color,"cyan")
            gra.fillRect(player.x,player.y,10,10);
            
            if len(enemys)<8 :
                if random.randint(1,10) == 5:
                    enemys.append(cl.miniBoss(random.randint(550,600),random.randint(5,490)));
                else:
                    enemys.append(cl.Enemy(random.randint(550,600),random.randint(5,490)));
            
            
            count =0;
            for i in range(len(enemys)):
                
                i -= count;
                
                gra.setColor(enemys[i].color);
                gra.fillRect(enemys[i].x,enemys[i].y,enemys[i].size,enemys[i].size);
                enemys[i].action();
                enemys[i].moveBullet();
        
                if enemys[i].checkHit(player):
                    gameFlg = mode.GameMode.GAMEOVER;
                    enemys = [];
                    break;
                if enemys[i].checkHitBullet(player):
                    player.level -= 1;
                    if player.level <1:
                        gameFlg = mode.GameMode.GAMEOVER;
                        enemys=[];
                    break;
                if player.checkHitBullet(enemys[i]):
                    enemys[i].hp -= player.level;
                    if enemys[i].hp < 1:
                        if enemys[i].color == "green":
                            gameScore += 40;
                        gameScore += 10;
                        if enemys[i].dropExp():
                            orbs.append(cl.expOrb(enemys[i].x,enemys[i].y));
                        enemys.pop(i);
                        count += 1;
                elif enemys[i].checkIsOut():
                    enemys.pop(i);
                    count += 1;
                for j in range(len(orbs)):
                    if player.checkHit(orbs[j]):
                        player.level += 1;
                        orbs.pop(j);
                        break;
                        
            player.moveBullet();
            drawBullet();
            drawOrb();
            gra.setColor("black");
            gra.drawText(550,10,"Score:"+str(gameScore),10);
            gra.drawText(25,10,"Level:"+str(player.level),10);
            if pushKeys[5]:
                gra.drawText(80,490,"player:"+str(player.x)+","+str(player.y)+" bulletsNum:"+str(len(player.bullets)+len(player.barrageBullet)),10);
                gra.drawText(245,490,"       movespeed:"+str(player.moveSpeed)+" reloadTime:"+str(player.reloadTime)+" orbs:"+str(len(orbs)),10);
            
        case mode.GameMode.BOSS:
            print();
        case mode.GameMode.GAMEOVER:
            gra.setColor("red");
            gra.drawText(300,150,"GameOver",100);
            gra.setColor("black");
            gra.drawText(300,250,"Push Enter to Play again",40); 
            if(pushKeys[5]):
                gameFlg=mode.GameMode.START;
                orbs = [];
                gameScore =0;
                player = cl.Player(20,20);
                
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