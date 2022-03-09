import random
import math
class Bullet:
    def __init__(self,x,y,direction):
        self.x = x;
        self.y = y;
        # 方向を表す　まっすぐなら0、上方向なら1、した方向なら-1
        self.direction = direction;
        

class Plane:
    
    def __init__(self,x,y,color):
        self.bullets = [];
        self.x = x;
        self.y = y;
        self.reloadTime = 0;
        self.color = color;
        
    def addBullet(self):
        self.bullets.append(Bullet(self.x+10,self.y+5,0));
    
    def checkHit(self,object):
        if (self.x - object.x)**2+(self.y-object.y)**2 <200 :
            return True;
        return False;
    
    def checkHitBullet(self,object):
        for i in range(len(self.bullets)):
            if object.checkHit(self.bullets[i]):
                self.bullets.pop(i);
                return True;
        return False;
                
            
class Player(Plane):
    def __init__(self, x, y):
        super().__init__(x, y,"blue");
        self.moveSpeed = 10;
        self.level = 1;
        self.barrageBullet = [];
    
    def moveBullet(self):
        count =0;
        for i in range(len(self.bullets)):
            
            i -= count;
            
            if self.bullets[i].x < 600:
                self.bullets[i].x += 10;
            else:
                self.bullets.pop(i);
                count += 1;       
        
        count = 0;
        for i in range(len(self.barrageBullet)):
            
            i -= count;
            
            if self.barrageBullet[i].x > 600 or self.barrageBullet[i].y < 0 or self.barrageBullet[i].y>500:
                self.barrageBullet.pop(i);
                count += 1;
            else:   
                if self.barrageBullet[i].direction > 0 :
                    self.barrageBullet[i].x += int(math.cos(math.radians(360-self.barrageBullet[i].direction*15))*10);
                    self.barrageBullet[i].y += int(math.sin(math.radians(360-self.barrageBullet[i].direction*15))*10);
                else:
                    self.barrageBullet[i].x += int(math.cos(math.radians(-self.barrageBullet[i].direction*15))*10);
                    self.barrageBullet[i].y += int(math.sin(math.radians(-self.barrageBullet[i].direction*15))*10);    
                
    def addBullet(self):
        
        super().addBullet();
        
        if self.level > 10 :
            self.barrageBullet.append(Bullet(self.x+10,self.y,1));
            self.barrageBullet.append(Bullet(self.x+10,self.y+10,-1));
            if self.level > 15:
                self.barrageBullet.append(Bullet(self.x+10,self.y,2));
                self.barrageBullet.append(Bullet(self.x+10,self.y+10,-2));
                if self.level > 20:
                    self.barrageBullet.append(Bullet(self.x+10,self.y,3));
                    self.barrageBullet.append(Bullet(self.x+10,self.y+10,-3));
                    if self.level > 25:
                        self.barrageBullet.append(Bullet(self.x+10,self.y,4));
                        self.barrageBullet.append(Bullet(self.x+10,self.y+10,-4));
                        if self.level > 30:
                            self.barrageBullet.append(Bullet(self.x+10,self.y,5));
                            self.barrageBullet.append(Bullet(self.x+10,self.y+10,-5));
                    
                    
                    
                
            
    def checkHitBullet(self, object):
        if super().checkHitBullet(object):
            return True;
        for i in range(len(self.barrageBullet)):
            if object.checkHit(self.barrageBullet[i]):
                self.barrageBullet.pop(i);
                return True;
        return False;
        


class Enemy(Plane):
    
    def __init__(self, x, y):
        super().__init__(x, y,"red");
        self.hp=5;
        self.size = 10;
    
    def action(self):
        if random.randint(1,5) > 2  and self.reloadTime == 0:
            self.addBullet();
            self.reloadTime = 10;
        else:
            self.move();
            self.reloadTime -= 1;
    
    def move(self):
        
        if(not self.checkIsOut()):
            self.x -= 5;
        
        
    def moveBullet(self):
        
        count =0;
        
        for i in range(len(self.bullets)):
            
            i -= count ;
            
            if self.bullets[i].x >0:
                self.bullets[i].x -= 7;
            else:
                self.bullets.pop(i);
                count += 1; 
    
    def checkIsOut(self):
        if(self.x<0):
            return True;
        return False;
    
    def dropExp(self):
        rand = random.randint(1,10);
        if rand == 2 :
            return True;
        elif self.color == "green" and rand >8:
            return True;
            
        return False;
    
            
class miniBoss(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y);
        self.hp = 15;
        self.color = "green";
        self.size = 15;
        
class Boss(Enemy):    
    def __init__(self, x, y):
        super().__init__(x, y);
        self.hp = 50;
        self.color = "black";
        self.size = 30;
    
class expOrb:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;   
    


        