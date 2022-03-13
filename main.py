
import sys
import random;
import tkinter
from turtle import back
import graphics
import gameMode as mode
import classes as cl;
import time;

# ウィンドウの生成
Root = tkinter.Tk();
# グラフィクスオブジェクトの生成
gra = graphics.Graphics(tkinter.Canvas(Root,width=600,height=500,bg="white"));

gameFlg =  mode.GameMode.START; 

player = cl.Player(20,20);

enemys = [];

boss = cl.Boss(450,250);

images = [tkinter.PhotoImage(file="img\Quu.png"),tkinter.PhotoImage(file="img\Sapphire.png")];
#           key.A key.D Key.W Key.S Key.K Key.Enter
pushKeys = [False,False,False,False,False,False];

orbs = [];

gameScore = 0;

startTime=0;
endTime =0;

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

        
def drawDubug():
    
    global gra;
    
    gra.setColor("black");
    
    gra.drawText(80,490,"player:"+str(player.x)+","+str(player.y)+" bulletsNum:"+str(len(player.bullets)+len(player.barrageBullet)),10);
    gra.drawText(245,490,"       movespeed:"+str(player.moveSpeed)+" reloadTime:"+str(player.reloadTime)+" orbs:"+str(len(orbs)),10);

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
    if gameFlg == mode.GameMode.BOSS:
        gra.setColor("black")
        for i in range(len(boss.cannnons)):
            for j in range(len(boss.cannnons[i].bullets)):
                gra.fillOval(boss.cannnons[i].bullets[j].x,boss.cannnons[i].bullets[j].y,radiusw=3,radiush=3);
        for i in range(len(boss.bullets)):
             gra.fillOval(boss.bullets[i].x,boss.bullets[i].y,radiusw = 3,radiush = 3);
                
            
def drawOrb():
    
    global gra;
    
    gra.setColor("yellow");
    
    for i in range(len(orbs)):
        gra.fillOval(orbs[i].x,orbs[i].y,4,4);
        
    
def drawBoss():
    global gra;
    
    gra.setLineColor("black")
    
    gra.setColor("black");
    
    gra.fillRect(boss.x-100,boss.y-100,200,60);
    gra.fillRect(boss.x,boss.y-40,100,80);
    gra.fillRect(boss.x-100,boss.y+40,200,60);
    
    gra.setBothColor(boss.color,"pink");
    gra.fillOval(boss.x,boss.y,10,10);
    
    if len(boss.cannnons) >0:
        gra.setBothColor(boss.cannnons[0].color,"black");
    
    for i in range(len(boss.cannnons)):
        gra.fillRect(boss.cannnons[i].x,boss.cannnons[i].y,10,10)
    gra.setLineColor("cyan");

def drawBossHpGauge():
    
    global gra;
    
    gra.setBothColor("gray","gray");
    
    gra.fillRect(10,0,500,10);
    
    bossHp = boss.hp//20;
    
    
    gra.setBothColor("red","red");
    
    gra.fillRect(10,0,bossHp,10)

def gameLoop():
    
    global gameFlg;
    global enemys;
    global player;
    global gameScore;
    global orbs;
    global startTime;
    global endTime;
    global boss;
    
    gra.clear();
    
    
    match(gameFlg):
        
        case mode.GameMode.START:
            gra.drawText(300,150,"Shooting",100);
            gra.drawText(300,250,"Push Enter to Play",50);
            gra.drawImage(550,450,images[1]); 
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
            if gameScore > 2000:
                enemys = [];
                orbs = [];
                player.bullets = [];
                player.barrageBullet = [];
                gameFlg = mode.GameMode.LOAD;
                startTime = time.time();
            if pushKeys[5]:
                drawDubug();
                
        case mode.GameMode.LOAD:
            gra.setBothColor(player.color,"cyan")
            gra.fillRect(player.x,player.y,10,10);
            if player.x == 100 and player.y == 250:
                endTime = time.time();
                if endTime - startTime > 10:
                    gra.setColor("red");
                    gra.drawText(300,150,"WARNING",100);
                    if endTime - startTime > 15:
                        player.level *= 3;
                        gameFlg = mode.GameMode.BOSS;
            else:
                if player.x < 100:
                    player.x += 1;
                elif player.y > 100:
                    player.x -= 1;
                
                if player.y < 250:
                    player.y += 1;
                elif player.y> 250:
                    player.y -= 1;
            
        case mode.GameMode.BOSS:
            
            playerAction();
            gra.setBothColor(player.color,"cyan")
            gra.fillRect(player.x,player.y,10,10);
            
            boss.action();
            
            count = 0;
            for i in range(len(boss.cannnons)):
                i -= count;
                boss.cannnons[i].action();
                if boss.cannnons[i].checkHitBullet(player):
                    player.level -= 1;
                    if player.level <1:
                        gameFlg = mode.GameMode.GAMEOVER;
                        break;
                if boss.cannnons[i].checkHit(player):
                    gameFlg = mode.GameMode.GAMEOVER;
                    break;
                if player.checkHitBullet(boss.cannnons[i]):
                    boss.cannnons[i].hp -= player.level;
                    if boss.cannnons[i].hp <1:
                        boss.cannnons.pop(i);
                        count +=1;        
            if boss.checkHitBullet(player):
                player.level -= 1;
                if player.level <1:
                    gameFlg = mode.GameMode.GAMEOVER;
            count = 0;
            for i in range(len(player.bullets)):
                """
                boss.x-100,boss.y-100,200,60
                boss.x,boss.y-40,100,80
                boss.x-100,boss.y+40,200,60"""
                i -= count;
                if (player.bullets[i].x> boss.x -100 and player.bullets[i].x < boss.x +100 and player.bullets[i].y > boss.y-100 and player.bullets[i].y < boss.y-40) or (player.bullets[i].x  > boss.x and player.bullets[i].x < boss.x +100 and player.bullets[i].y > boss.y-40 and player.bullets[i].y < boss.y+40) or (player.bullets[i].x > boss.x -100 and player.bullets[i].x < boss.x +100 and player.bullets[i].y > boss.y+40 and player.bullets[i].y < boss.y+100):
                    player.bullets.pop(i);
                    count +=1;back
            count = 0;
            for i in range(len(player.barrageBullet)):
                """
                boss.x-100,boss.y-100,200,60
                boss.x,boss.y-40,100,80
                boss.x-100,boss.y+40,200,60"""
                i -= count;
                if (player.barrageBullet[i].x> boss.x -100 and player.barrageBullet[i].x < boss.x +100 and player.barrageBullet[i].y > boss.y-100 and player.barrageBullet[i].y < boss.y-40) or (player.barrageBullet[i].x  > boss.x and player.barrageBullet[i].x < boss.x +100 and player.barrageBullet[i].y > boss.y-40 and player.barrageBullet[i].y < boss.y+40) or (player.barrageBullet[i].x > boss.x -100 and player.barrageBullet[i].x < boss.x +100 and player.barrageBullet[i].y > boss.y+40 and player.barrageBullet[i].y < boss.y+100):
                    player.barrageBullet.pop(i);
                    count +=1;
            if (player.x+10> boss.x -100 and player.x+10 < boss.x +100 and player.y+10 > boss.y-100 and player.y+10 < boss.y-40) or (player.x+10  > boss.x and player.x+10 < boss.x +100 and player.y+10 > boss.y-40 and player.y+10 < boss.y+40) or (player.x+10 > boss.x -100 and player.x+10 < boss.x +100 and player.y+10 > boss.y+40 and player.y+10 < boss.y+100):
                gameFlg = mode.GameMode.GAMEOVER;
            if player.checkHitBullet(boss):
                boss.hp -= player.level;
                if boss.hp < 1:
                    gameFlg = mode.GameMode.CLEAR;
                    gameScore = gameScore +10000+ player.level*100  
            drawBoss();
            player.moveBullet();
            drawBullet();
            
            gra.drawText(550,10,"Level:"+str(player.level),10);
            
            drawBossHpGauge();
            
            if pushKeys[5]:
                drawDubug();
                
        case mode.GameMode.GAMEOVER:
            gra.setColor("red");
            gra.drawText(300,150,"GameOver",100);
            gra.setColor("black");
            gra.drawText(300,250,"Push Enter to Play again",40); 
            if(pushKeys[5]):
                gameFlg=mode.GameMode.START;
                orbs = [];
                boss = cl.Boss(450,250);
                gameScore =0;
                player = cl.Player(20,20);
                
        case mode.GameMode.CLEAR:
            gra.setColor("yellow");
            gra.drawText(300,150,"GameClear",100);
            gra.setColor("black");
            gra.drawText(300,250,"Score:"+str(gameScore),40); 
            gra.drawImage(550,450,images[1]); 
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