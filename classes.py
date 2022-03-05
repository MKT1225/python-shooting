class Plane:
    
    def __init__(self,x,y,hp):
        self.bullets = [];
        self.x = x;
        self.y = y;
        self.hp=hp;
        
    def addBullet(self,x,y):
        self.bullets.append(Bullet(x,y));
        
    
class Player(Plane):
    def __init__(self, x, y,hp):
        super().__init__(x, y,hp);

class Enemy(Plane):
    def __init__(self, x, y,hp):
        super().__init__(x, y,hp);
        
class Boss(Enemy):    
    def __init__(self, x, y,hp):
        super().__init__(x, y,hp);
    
class Bullet:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
        
    


        