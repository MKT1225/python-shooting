import random;
class Plane:
    
    def __init__(self,x,y,hp,color):
        self.bullets = [];
        self.x = x;
        self.y = y;
        self.hp=hp;
        self.reloadTime = 0;
        self.color = color;
        
    def addBullet(self):
        self.bullets.append(Bullet(self.x+10,self.y+5));
    
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
        super().__init__(x, y,10,"blue");
        self.moveSpeed = 10;
    
    def moveBullet(self):
        count =0;
        for i in range(len(self.bullets)):
            
            i -= count;
            
            if self.bullets[i].x < 600:
                self.bullets[i].x += 10;
            else:
                self.bullets.pop(i);
                count += 1; 
                
    
    

class Enemy(Plane):
    
    def __init__(self, x, y):
        super().__init__(x, y,5,"red");
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
    
class Bullet:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
        
        
    


        