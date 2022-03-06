
class Plane:
    
    def __init__(self,x,y,hp):
        self.bullets = [];
        self.x = x;
        self.y = y;
        self.hp=hp;
        self.reloadTime = 0;
        
    def addBullet(self):
        self.bullets.append(Bullet(self.x+10,self.y+5));
    
    def checkHit(self,object):
        if (self.x - object.x)**2+(self.y-object.y)**2 <150 :
            return True;
        return False;
    
    def checkHitBullet(self,object):
        for i in range(len(self.bullets)):
            if object.checkHit(self.bullets[i]):
                self.bullets.pop(i);
                return True;
        return False;
                
            
class Player(Plane):
    def __init__(self, x, y,hp):
        super().__init__(x, y,hp);
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
    def __init__(self, x, y,hp):
        super().__init__(x, y,hp);
    
    def move(self):
        
        if(not self.checkIsOut()):
            self.x -= 5;
        
        
    def moveBullet(self):
        
        count =0;
        
        for i in range(len(self.bullets)):
            
            i -= count ;
            
            if self.bullets[i].x >0:
                self.bullets[i].x -= 3;
            else:
                self.bullets.pop(i);
                count += 1; 
    
    def checkIsOut(self):
        if(self.x<0):
            return True;
        return False;
    
            
        
        
class Boss(Enemy):    
    def __init__(self, x, y,hp):
        super().__init__(x, y,hp);
    
class Bullet:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
        
    


        